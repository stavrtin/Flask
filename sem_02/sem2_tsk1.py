from pathlib import PurePath, Path

from flask import Flask, request, abort, redirect, url_for, flash
from flask import render_template
from werkzeug.utils import secure_filename
from markupsafe import escape

app = Flask(__name__)

app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def start():
    return render_template("start.html")


@app.route('/page1')
def df_page1():
    return "Привет Вася"


@app.route('/load_i', methods=['GET', 'POST'])
def load_img():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        # return f"Файл {escape(file_name)} загружен на сервер"
        return f"Файл {(file_name)} загружен на сервер"

    context = {
        'task': 'Задание_2',
    }

    return render_template("page1.html", **context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    users = {
        'auth_email': '1@mail.ru',
        'auth_pass': '123',
    }
    if request.method == 'POST':
        auth_email = request.form.get('auth_email')
        auth_pass = request.form.get('auth_pass')
        if auth_email == users['auth_email'] and auth_pass == users['auth_pass']:
            # page_after_login.html
            # return f"Вход с почты {auth_email} выполнен успешно"
            data = {"data_mail": auth_email,
                    "data_pass": auth_pass}
            return render_template("page_after_login.html", **data)
        else:
            return f"Ошибка страницы 404"
    context = {'task': 'Задание_3'}
    return render_template("autorization.html", **context)


@app.route('/text_len', methods=['GET', 'POST'])
def text_len():
    if request.method == 'POST':
        text_ar = request.form.get('textarea_input')
        data = {'count_words': len(text_ar.split())}
        return render_template("after_text.html", **data)
    context = {
        'task': 'Задание_4',
    }
    return render_template("text.html", **context)


@app.route('/arifmetics', methods=['GET', 'POST'])
def arifmetics():
    if request.method == 'POST':
        number1 = request.form.get('number_1')
        number2 = request.form.get('number_2')
        znak = request.form.get('oper')
        if znak == 'add':
            return str(int(number1) + int(number2))
        elif znak == 'subtract':
            return str(int(number1) - int(number2))
        elif znak == 'mult':
            return str(int(number1) * int(number2))
        elif znak == 'divig':
            # else:
            return str(int(number1) / int(number2))

    context = {
        'task': 'Задание_5',
    }
    return render_template("arifmetics_page.html", **context)


@app.route('/age', methods=['GET', 'POST'])
def age():
    MIN_AGE = 18
    if request.method == 'POST':
        name_user = request.form.get('input_name')
        age_user = request.form.get('input_age')
        if int(age_user) < MIN_AGE:
            abort(403)
        else:
            return f'{name_user}, вы вошли'
    context = {
        'task': 'Задание_6',
    }
    return render_template("age_page.html", **context)


@app.errorhandler(403)
def page_not_found(e):
    context = {
        'title': 'Возраст менее 18, доступ закрыт',
        'url': request.base_url,
    }
    return render_template('403_1.html', **context), 403


@app.route('/squadr', methods=['GET', 'POST'])
def redirect_squadr():
    if request.method == 'POST':
        number_sqr = (request.form.get('input_number'))
        return redirect(url_for('q_res1', number=number_sqr))
    context = {
        'task': 'Задание_7',
    }
    return render_template("sqr_page.html", **context)


@app.route('/squadr/<number>')
def q_res1(number):
    dd = number
    return str(int(dd) ** 2)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
    # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
