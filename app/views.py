from flask import render_template, redirect, url_for, flash, request, jsonify
from werkzeug.security import generate_password_hash

from app import app
from app.models import User, Group, GroupTaskStatus, Task
from app.forms import LoginForm, RegisterForm, TaskForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import db
from urllib.parse import urlsplit


@app.route("/")
def home():
    return render_template('home.html', title="Welcome Home :)")

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        flash("You are already registered/logged in!", 'error')
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_check = db.session.scalar(db.select(User).where(User.student_id==form.student_id.data))
        if user_to_check == None:
            flash("Entered credentials do no match our records - please check and try again", "danger")
            return redirect(url_for('registration'))
        if user_to_check.email != form.email.data:
            flash("Entered credentials do no match our records - please check and try again", "danger")
            return redirect(url_for('registration'))
        if user_to_check.registered == True:
            flash("You are already registered in the system! Head on to the mobile app and meet some new people!", "danger")
            return redirect(url_for('registration'))
        user_to_check.password_hash = generate_password_hash(form.password.data)
        user_to_check.registered = True
        db.session.commit()
        flash("You have successfully registered with Mix&Match. Head over to the mobile app and have a go at meeting new people!", "success")
        return redirect(url_for("registration"))
    return render_template('registration.html', title="Student registration", form=form)




@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
        if user.role != "Admin":
            flash("Only admins can use the online portal. For student and mentor access use the mobile Mix&Match app", "danger")
            return redirect("login")
        if not user.check_password(form.password.data):
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
                'status': task_status.status,
                'start_datetime' : task_status.task.start_datetime,
                'end_datetime' : task_status.task.end_datetime,
                'location' : task_status.task.location
            }
            group_response['tasks'].append(task)
    except Exception:
        return jsonify({'tasks': []}), 200

    return jsonify(group_response), 200

@app.route('/create_task', methods=['GET', 'POST'])
@login_required
def create_task():
    if current_user.role != "Admin":
        flash("Only admin users are allowed on that page", "danger")
        return redirect(url_for("home"))
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, description=form.description.data, isUpload=form.isUpload.data, start_datetime=form.start_datetime.data, end_datetime=form.end_datetime.data, location=form.location.data)
        db.session.add(task)
        db.session.flush()
        all_group_ids = db.session.scalars(db.select(Group.id)).all()
        for group_id in all_group_ids:
            db.session.add(GroupTaskStatus(task_id=task.id, group_id=group_id))
        db.session.commit()
        flash("Task created successfully",'success')
        return redirect(url_for('create_task'))
    return render_template('create_task.html', title="Create a new task", form=form)


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


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


# Error handlers
# See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# Error handler for 403 Forbidden
@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html', title='Error 403'), 403


# Handler for 404 Not Found
@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html', title='Error 404'), 404


@app.errorhandler(413)
def error_413(error):
    return render_template('errors/413.html', title='Error 413'), 413


# 500 Internal Server Error
@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html', title='Error 500'), 500
