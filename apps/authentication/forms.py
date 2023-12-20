# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import Email, DataRequired, Length


# login and registration


class LoginForm(FlaskForm):
    username = StringField('Username',
                           id='username_login',
                           validators=[DataRequired(), Length(3, 10)])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired(), Length(6)])


class CreateAccountForm(FlaskForm):
    username = StringField('Username',
                           id='username_create',
                           validators=[DataRequired(), Length(3, 10)])
    email = EmailField('Email',
                       id='email_create',
                       validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired(), Length(6)])
