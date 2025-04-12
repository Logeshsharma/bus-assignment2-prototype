from flask import render_template, redirect, url_for, flash, request, jsonify
from app import app
from app.models import User, Group, GroupTaskStatus
from app.forms import LoginForm, ChooseForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import db
from urllib.parse import urlsplit
import random


@app.route("/")
def home():
    return render_template('home.html', title="Welcome Home :)")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('generic_form.html', title='Sign In', form=form)


@app.route('/login_mobile', methods=['GET', 'POST'])
def login_mobile():
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        user = db.session.scalar(
            sa.select(User).where(User.username == username))

        if user is None or not user.check_password(password):
            return jsonify({"message": "Login failed. Invalid username or password", "status": "error"}), 401

        return jsonify(
            {"message": "Login successful", "status": "success", "id": user.id, "username": user.username,
             "email": user.email, "role": user.role, "groupId": user.group_id, }), 200


@app.route('/get_group_mobile/<int:group_id>')
def get_group_mobile(group_id):
    try:
        group = db.session.get(Group, group_id)
        group_response = {
            'group_id': group.id,
            'users': [user.to_dict() for user in group.users]
        }
        if group is None:
            return jsonify({'id': -1}), 200
    except Exception:
        return jsonify({'id': -1}), 200

    return jsonify(group_response), 200


@app.route('/get_tasks_mobile/<int:group_id>')
def get_tasks_mobile(group_id):
    try:
        q = db.select(Group).where(Group.id == group_id)
        group = db.session.scalar(q)
        if not group:
            return jsonify({'message': 'No Group'}), 404
        group_response = {
            'group_id': group.id,
            'tasks': []
        }
        for task_status in group.taskstatus:
            task = {
                'id': task_status.task.id,
                'title': task_status.task.title,
                'desc': task_status.task.description,
                'isUpload': task_status.task.isUpload,
                'status': task_status.status
            }
            group_response['tasks'].append(task)
    except Exception:
        return jsonify({'tasks': []}), 200

    return jsonify(group_response), 200


@app.route('/update_task_status', methods=['GET', 'POST'])
def update_task_status():
    try:
        if request.method == 'POST':
            group_id = request.json.get('group_id')
            task_id = request.json.get('task_id')
            status = request.json.get('status')
            task_status = db.session.get(GroupTaskStatus, (group_id, task_id))
            task_status.status = status
            db.session.commit()
    except Exception:
        return jsonify({'status': 'failed'}), 404

    return jsonify({'status': 'Updated'}), 200



@app.route('/admin_account', methods=['GET', 'POST'])
@login_required
def admin_account():
    form = ChooseForm
    if current_user.is_authenticated and current_user.role == 'Admin':
        q = sa.select(User)
        all_users = db.session.scalars(q).all()
        regist_status = {0:'False', 1:'True'}
        return render_template('admin_account.html', title='Admin Account', all_users=all_users, regist_status=regist_status, form=form)
    else:
        flash(f'{current_user.username} you are not admin. Access denied', 'danger')
    return redirect(url_for('home'))

@app.route('/group_generation', methods=['GET', 'POST'])
def group_generation():

    eligible_users = User.query.filter(User.registered == 1, User.role != 'Admin', User.group_id == None).all()
    if len(eligible_users) < 4:
        flash(f'Sorry You already made groups once. So not enough users registered available', 'danger')
        return redirect(url_for('home'))
    else:
        students = [user for user in eligible_users if user.role == 'Student']
        mentors = [user for user in eligible_users if user.role == 'Mentor']
        print('Student list:', students)
        print('Mentors list:', mentors)
        num_groups = min(len(students) // 4, len(mentors))
        print(num_groups)
        random.shuffle(students)
        random.shuffle(mentors)

        selected_mentor = random.sample(mentors, num_groups)
        print('Mentors list:', selected_mentor)
        for i in range(num_groups):
            selected_students = random.sample(students, 4)
            print(f'Student list{i}:', selected_students)
            group = Group()
            mentor = random.choice(selected_mentor)
            print(f'Mentor{i}:', mentor)
            # mentor.group = group
            group.users.clear()
            group.users.append(mentor)
            group.users.extend(selected_students)

            db.session.add(group)
            db.session.commit()
            selected_mentor.remove(mentor)
            print(f'Mentor removed {i}:', mentor)
            for student in selected_students:
                students.remove(student)
            print(f'Student removed list{i}:', selected_students)

        q = sa.select(Group)
        all_groups = db.session.scalars(q).all()
        flash('Groups Successfully Generated', 'success')

    return render_template('group_generation.html', title='First Groups Page', all_groups=all_groups)

@app.route('/group', methods=['GET'])
def group():
    q = sa.select(Group)
    all_groups = db.session.scalars(q).all()
    for group in all_groups:
        group.users.sort(key=lambda user: 0 if user.role == 'Mentor' else 1)
    print('Groups list:',all_groups)
    return render_template('group.html', title='Group Page', all_groups=all_groups)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


# Error handlers
# See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# Error handler for 403 Forbidden
@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html', title='Error'), 403


# Handler for 404 Not Found
@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html', title='Error'), 404


@app.errorhandler(413)
def error_413(error):
    return render_template('errors/413.html', title='Error'), 413


# 500 Internal Server Error
@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html', title='Error'), 500
