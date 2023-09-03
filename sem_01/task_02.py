from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Про новости!'

@app.route('/news')
def news_index():
    news_block = [
        {'title':    'Новость - 1 ',
         'body_news': 'Что-то про что-то 1111',
         'data_public': datetime.now().strftime('%H:%M - %d.%m.%Y год')},
        {'title': 'Новость - 2 ',
         'body_news': 'Что-то про что-то 222',
         'data_public': datetime.now().strftime('%H:%M - %d.%m.%Y год')},
        {'title': 'Новость - 3 ',
         'body_news': 'Что-то ро что-то 3333',
         'data_public': datetime.now().strftime('%H:%M - %d.%m.%Y')},

    ]
    new_contant = { 'news_task': news_block }

    return render_template('index_2.html', **new_contant)

if __name__ == '__main__':
    app.run(debug=True)