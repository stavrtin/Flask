from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/about/')
def text_ab():
    return 'about'

@app.route('/contact/')
def text_cont():
    return 'contact'


@app.route('/<int:num_1>/<int:num_2>')
def sum_nums(num_1: int, num_2: int) -> str:
    return str(num_1 + num_2)

@app.route('/string/<string:stroka>')
def len_str(stroka: str) -> str:
    return str(len(stroka))

@app.route('/text')
def index_text():
    return render_template('index_1.html')


@app.route('/stud')
def index_stud():
    head = {
        'name': 'Имя',
        'lastname': 'Фам',
        'age':'Возраст',
        'raiting':'Србал'
            }
    _student = [
        {'name':    'Вася_1',
         'lastname': 'Фам_1',
         'age':     12,
         'raiting': 3.2},
        {'name': 'Вася_2',
         'lastname': 'Фам_2',
         'age': 13,
         'raiting': 5.2},
        {'name': 'Вася_3',
         'lastname': 'Фам_3',
         'age': 15,
         'raiting': 1.2},
    ]
    contant = { 'student': _student }

    return render_template('index_1.html', **contant)

if __name__ == '__main__':
    app.run(debug=True)