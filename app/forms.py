from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, StringField, PasswordField, BooleanField, SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, EqualTo, NumberRange, ValidationError, Email, Optional, Length
from app import db
from app.models import User
import datetime


class ChooseForm(FlaskForm):
    choice = HiddenField('Choice')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class TaskForm(FlaskForm):
    title = StringField("Task title", validators=[DataRequired(), Length(min=1, max=64, message="Task description must be no longer than 64 characters")])
    description = StringField("Task description", validators=[DataRequired(), Length(min=1, max=1024, message="Task description must be no longer than 1024 characters")])
    isUpload = BooleanField("Task requires file upload for verification and completion")
    submit = SubmitField("Create task")