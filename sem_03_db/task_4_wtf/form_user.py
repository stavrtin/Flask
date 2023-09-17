from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo


# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired()])
#     password = PasswordField('Password',  validators=[DataRequired()])

class RegisterForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password'
                           , validators=[DataRequired()])
    confirm_pass = StringField('ConfPassword', validators=[DataRequired(),  EqualTo('password')])