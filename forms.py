from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                                Length, EqualTo)

from models import User


def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('User with that username already exists.')


def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('That email is already registered.')


class RegistrationForm(Form):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            name_exists,
            Regexp(
                r'^[a-zA-Z0-9_]+$',
                message=("Username should be one word, letters, "
                         "numbers, and underscores only.")
            )
        ]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=5),
            EqualTo('password2', message='Passwords must match')
        ]
    )
    password2 = PasswordField(
        'Confirm Password', validators=[DataRequired()]
    )


class LoginForm(Form):
    email = StringField(
        'Email', validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Password', validators=[DataRequired()]
    )


class CreateGame(Form):
    game_title = StringField(
        'Game Title',
        validators=[DataRequired(), Length(max=100)])


class GameSession(Form):
    session_notes = TextAreaField('Session Notes', validators=[DataRequired()])
