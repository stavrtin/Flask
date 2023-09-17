from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_users.db'
db = SQLAlchemy(app)

'''Задание №4
📌 Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна 
содержать следующие поля:
○ Имя пользователя (обязательное поле)
○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
📌 После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite) 
и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не 
заполнено или данные не прошли валидацию, то должно выводиться соответствующее 
сообщение об ошибке. 
📌 Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в 
базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение 
об ошибке..'''


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(80), nullable=False)
#     def __repr__(self):
#         return f'(Книга "{self.name}" )'
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80),  nullable=False)
    password = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return f'({self.name}+{self.email}+{self.password} )'


