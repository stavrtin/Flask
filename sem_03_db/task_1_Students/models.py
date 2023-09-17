from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_db_facultets.db'
db = SQLAlchemy(app)

'''Задание №1
📌 Создать базу данных для хранения информации о студентах университета. 
📌 База данных должна содержать две таблицы: "Студенты" и "Факультеты". 
📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, 
возраст, пол, группа и id факультета. 
📌 В таблице "Факультеты" должны быть следующие поля: id и название 
факультета. 
📌 Необходимо создать связь между таблицами "Студенты" и "Факультеты". 
📌 Написать функцию-обработчик, которая будет выводить список всех 
студентов с указанием их факультета.'''


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

    def __repr__(self):
        return f'({self.firstname} {self.lastname})'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fac_name = db.Column(db.String(80), nullable=False)
    students = db.relationship('Student', backref='faculty', lazy=True)

    def __repr__(self):
        return f'({self.fac_name})'


# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     bookname = db.Column(db.String(80), nullable=False)
#     year_at = db.Column(db.String(80), nullable=False)
#     count_exempl = db.Column(db.Integer, nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
#     author_name = db.relationship('Author', backref='author_name', lazy=True)
#
#     def __repr__(self):
#         return f'(Книга "{self.bookname}" автора {self.author_name} )'
#
#
# class Author(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     firstname = db.Column(db.String(80), nullable=False)
#     lastname = db.Column(db.String(80), nullable=False)
#
#     def __repr__(self):
#         return f'(Автор {self.lastname})'