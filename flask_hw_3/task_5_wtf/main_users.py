from flask import Flask, render_template, request, redirect, flash, url_for
from task_5_wtf.models_db_users import db, User
from task_5_wtf.form_user import  RegisterForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_users_t5.db'
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
db.init_app(app)


# --------------------создание таблиц и наполнение данными ---------------
@app.cli.command('init-db-user')
def init_db():
    db.create_all()
    print('ok')

@app.route('/')
def start():
    return 'Поехали!'


@app.route('/lib')
def lib():
    user_base = User.query.all()
    content = {'users_1': user_base}
    return render_template('user_base_librery.html', **content)


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        # как обработать форму
        username_f = form.name.data
        email_f = form.email.data
        password_f = form.password.data
        bearthday_f = form.bearthday.data
        soglasie_f = form.soglasie.data

        user = User(
                name=username_f,
                email=email_f,
                password=password_f,
                bearthday=bearthday_f,
                soglasie=soglasie_f,
            )
        user.set_password(password_f)
        db.session.add(user)
        db.session.commit()
        flash('Форма успешно отправлена!', 'success')
        return redirect('/userview')
    return render_template('registr.html', form=form)


@app.route('/userview')
def userview():
    user_base = User.query.all()
    content = {'users_v': user_base}
    return render_template('user_base_librery.html', **content)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('registr.html'))
    return render_template('user_base_librery.html')


if __name__ == '__main__':
    app.run(debug=True)
