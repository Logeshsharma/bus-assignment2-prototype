from flask import render_template, redirect, url_for, flash, request, send_file, send_from_directory, jsonify
from app import app
from app.models import User, Group
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required, fresh_login_required
import sqlalchemy as sa
from app import db
from urllib.parse import urlsplit


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


@app.route('/mobile_login', methods=['GET', 'POST'])
def mobile_login():
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        user = db.session.scalar(
            sa.select(User).where(User.username == username))

        if user is None or not user.check_password(password):
            return jsonify({"message": "Login failed. Invalid username or password", "status": "error"}), 401

        return jsonify(
            {"message": "Login successful", "status": "success", "userId": user.id, "username": user.username,
             "email": user.email, "role": user.role, }), 200


@app.route('/get_group/<int:group_id>')
def get_group(group_id):
    try:
        group = db.session.get(Group, group_id)
        if group is None:
            return jsonify({'id': -1}), 200
    except Exception:
        return jsonify({'id': -1}), 200

    return jsonify(group.to_dict()), 200


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
