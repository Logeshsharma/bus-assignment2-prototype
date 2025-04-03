from flask import render_template, redirect, url_for, flash, request, send_file, send_from_directory, jsonify
from app import app
from app.models import User, Book, Loan
from app.forms import ChooseForm, LoginForm
from flask_login import current_user, login_user, logout_user, login_required, fresh_login_required
import sqlalchemy as sa
from app import db
from urllib.parse import urlsplit
import csv
import io
import datetime


@app.route("/")
def home():
    return render_template('home.html', title="Welcome Home :)")


@app.route("/account")
@login_required
def account():
    chooseForm = ChooseForm()
    q = db.select(User).where(User.id == current_user.id)
    user = db.session.scalar(q)
    loans = user.loans
    return render_template('account.html', title="Account", loans=loans, chooseForm=chooseForm)


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


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/all_books')
def all_books():
    books = []
    try:
        books.append(
            ['Id', 'Title', 'Author', 'Genre', 'Summary', 'Published year', 'Book availability'])
        query = db.select(Book)
        books.extend(db.session.scalars(query).all())
    except Exception as e:
        flash(f'Something went wrong {e}', 'danger')

    return render_template('books.html', title='Books', books=books)


@app.route('/book_details/<int:book_id>', methods=['GET', 'POST'])
def book_details(book_id):
    book = db.session.get(Book, book_id)

    if book is None:
        flash("We're screwed", "danger")

    return render_template('book_details.html', title='Book Details', book=book)


@app.route('/delete_book', methods=['GET', 'POST'])
def delete_book():
    form = ChooseForm()
    if form.validate_on_submit():
        q = db.select(Loan).where(Loan.book_id == int(form.choice.data) and Loan.user_id == current_user.id)
        loan = db.session.scalar(q)
        print(loan)
        try:
            db.session.delete(loan)
            db.session.commit()
            flash('Loan returned', 'info')
        except Exception:
            db.session.rollback()
            flash('Something went wrong', 'danger')

    return redirect(url_for('account'))


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
