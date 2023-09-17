from flask import Flask, render_template
from task_2_books.models_db_book import db, Book, Author, BookAuthor

# from task_2_books.models_03 import db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_users.db'
db.init_app(app)


# --------------------создание таблиц и наполнение данными ---------------
@app.cli.command('init-db-user')
def init_db():
    db.create_all()
    print('ok')


@app.cli.command('add-users')
def add_author():
    author = Author(
        firstname='Александра',
        lastname='Пушкин')
    db.session.add(author)
    db.session.commit()
    print('Запись добавлена')


@app.route('/')
def start():
    return 'Поехали!'


@app.route('/books')
def books():
    books = Book.query.all()
    content = {'books': books}
    return render_template('user_base_librery.html', **content)


if __name__ == '__main__':
    app.run(debug=True)
