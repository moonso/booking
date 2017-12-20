from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, BooleanField, SubmitField)
from wtforms.validators import (DataRequired, ValidationError, Email, EqualTo)
from booking.models import User

from booking import app


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = app.config['USERS_COLLECTION'].find_one({"_id": username.data})
        if user is not None:
            raise ValidationError("Username already exists")
    
    def validate_email(self, email):
        user = app.config['USERS_COLLECTION'].find_one({"email": email.data})
        if user is not None:
            raise ValidationError("Email already exists")
        