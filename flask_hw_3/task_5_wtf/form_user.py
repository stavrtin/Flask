from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, DateField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    confirm_pass = StringField('ConfPassword', validators=[DataRequired(),  EqualTo('password')])
    bearthday = DateField('Bearthday', validators=[DataRequired()])
    # soglasie = SelectField('Soglasie', choices=[('male', 'Мужчина'), ('female', 'Женщина')], validators=[DataRequired()])
    soglasie = SelectField('Soglasie', choices=[('да'), ('нет')], validators=[DataRequired()])
