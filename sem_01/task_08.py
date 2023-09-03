from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html')


@app.route('/about/')
def about():
    return render_template('clothing.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)
