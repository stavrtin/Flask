from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_db_books.db'
db = SQLAlchemy(app)

'''Задание №2
📌 Создать базу данных для хранения информации о книгах в библиотеке. 
📌 База данных должна содержать две таблицы: "Книги" и "Авторы". 
📌 В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id автора.
📌 В таблице "Авторы" должны быть следующие поля: id, имя и фамилия. 
📌 Необходимо создать связь между таблицами "Книги" и "Авторы". 
📌 Написать функцию-обработчик, которая будет выводить список всех книг с указанием их авторов.'''


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookname = db.Column(db.String(80), nullable=False)
    year_at = db.Column(db.String(80), nullable=False)
    count_exempl = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    authors = db.relationship('Author', secondary='book_author', backref='books', lazy=True)

    def __repr__(self):
        return f'(Книга "{self.bookname}" )'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'(Автор {self.lastname})'


class BookAuthor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

# //////////////
