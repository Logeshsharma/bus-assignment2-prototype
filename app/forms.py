from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, StringField, PasswordField, BooleanField, SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, EqualTo, NumberRange, ValidationError, Email, Optional, Length
import re


def isUniversityEmail(form, field):
    if not field.data.endswith("@student.bham.ac.uk"):
        raise ValidationError("Email must be the student university email ending with \"@student.bham.ac.uk\"")

def hasUppercase(form, field):
    password = field.data
    if not re.search(r'[A-Z]', password):
        raise ValidationError("Password must have at least one uppercase character")

def hasLowercase(form, field):
    password = field.data
    if not re.search(r'[a-z]', password):
        raise ValidationError("Password must have at least one lowercase character")

def hasSpecialCharacter(form, field):
    password = field.data
    if not re.search(r'[^a-zA-Z0-9]', password):
        raise ValidationError("Password must have at least one special character")

class ChooseForm(FlaskForm):
    choice = HiddenField('Choice')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    student_id = IntegerField("Student ID number", validators=[DataRequired(message="A numerical value is required"), NumberRange(min=1000000, max=99999999, message="Student ID must be between 7 and 8 digits")])
    username = StringField("First name and Last name separated by a space", validators=[DataRequired(), Length(min=1, max=64, message="Username must be between 1 and 64 characters")])
    email = StringField("University email address", validators=[DataRequired(), isUniversityEmail])
    password = PasswordField("Type in your new account password", validators=[DataRequired(), hasLowercase, hasUppercase, hasSpecialCharacter, Length(min=8, max=64, message="Password length must be between 8 and 64 characters")])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), EqualTo('password', 'Passwords do not match')])
    submit = SubmitField("Register")



