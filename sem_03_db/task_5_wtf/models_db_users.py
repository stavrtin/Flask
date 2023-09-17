from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


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


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80),  nullable=False)
    password = db.Column(db.String(80), nullable=False)
    bearthday = db.Column(db.String(80), nullable=False)
    soglasie = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return f'({self.name}  )'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        self.password = check_password_hash(self.password, password)