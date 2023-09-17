from flask import Flask, render_template, request, redirect
from task_4_wtf.models_db_users import db, User
from flask_wtf import FlaskForm
from form_user import RegisterForm
from flask_wtf.csrf import CSRFProtect


# from task_2_books.models_03 import db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_users.db'
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
db.init_app(app)


# --------------------создание таблиц и наполнение данными ---------------
@app.cli.command('init-db-user')
def init_db():
    db.create_all()
    print('ok')


# @app.cli.command('add-user')
# def add_author():
#     user = User(
#         name='Александр',
#         email='asdasdasfsdf.rt',
#         password='123',
#     )
#     db.session.add(user)
#     db.session.commit()
#     print('Запись добавлена')


@app.route('/')
def start():
    return 'Поехали!'


@app.route('/lib')
def lib():
    user_base = User.query.all()
    content = {'users_1': user_base}
    return render_template('user_base_librery.html', **content)


@app.route('/registrated', methods=['GET', 'POST'])
def registrated():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        # как обработать форму
        username_f = form.name.data
        email_f = form.email.data
        password_f = form.password.data

        user = User(
                name=username_f,
                email=email_f,
                password=password_f,
            )
        db.session.add(user)
        db.session.commit()
        return redirect('/userview')
        # content = {'users_1': user_base}
    return render_template('registr.html', form=form)


@app.route('/userview')
def userview():
    user_base = User.query.all()
    content = {'users_v': user_base}
    return render_template('user_base_librery.html', **content)

if __name__ == '__main__':
    app.run(debug=True)
