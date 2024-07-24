from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, PasswordField, validators
from wtforms.validators import DataRequired

# The form is basic containing only two fields, both fields are string fields.
class addForm(FlaskForm):
    text1 = StringField('text1', [validators.DataRequired()])
    text2 = StringField('text2', [validators.DataRequired()])
    text3 = StringField('text3', [validators.DataRequired()])

class modifyEntry(FlaskForm):
    title = StringField('title', [validators.DataRequired()])
    review = TextAreaField('review', [validators.DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('username', [validators.DataRequired()])
    password = PasswordField('password', [validators.DataRequired()])

class RegistrationForm(FlaskForm):
    username = StringField('username', [validators.DataRequired()])
    email = StringField('email', [validators.DataRequired()])
    password = PasswordField('password', [validators.DataRequired()])
