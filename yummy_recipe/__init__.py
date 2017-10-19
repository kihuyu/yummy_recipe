from .yummy_recipe import app
from wtforms import Form, BooleanField, TextField, PasswordField, validators

class Registration(Form):
    username = TextField('Username')
    name = TextField('Email Address')
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
