from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, StringField, PasswordField, BooleanField, SelectField
from wtforms.fields.datetime import DateTimeField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, EqualTo, NumberRange, ValidationError, Email, Optional, Length
from app import db
from app.models import User
import datetime

# def isLaterThan(time=None, message="This field must have a later date"):
#     def _validator(form, field):
#         comparison_time = time or datetime.datetime.now()
#         if not field.data:
#             return
#         if field.data <= comparison_time:
#             raise ValidationError(message)
#     return _validator

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
    location = StringField("Location", validators=[DataRequired(), Length(min=1, max=128, message="Location name length is limited by 128 characters.")])
    start_datetime = DateTimeField("Event starting time", format="%Y-%m-%dT%H:%M", validators=[DataRequired()], render_kw={"type": "datetime-local"})
    end_datetime = DateTimeField("Event ending time", format="%Y-%m-%dT%H:%M", validators=[DataRequired()], render_kw={"type": "datetime-local"})
    isUpload = BooleanField("Task requires file upload for verification and completion")
    submit = SubmitField("Create task")

    def validate_start_datetime(form, field):
        if field.data <= datetime.datetime.now():
            raise ValidationError("Task start must be set in the future")

    def validate_end_datetime(form, field):
        if field.data <= form.start_datetime.data:
            raise ValidationError("Task end time must be after start time.")