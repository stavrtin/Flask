from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from form_1 import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/data')
def data():
    return 'My data!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # как обработать форму
        pass
    return render_template('login.html', form=form)





if __name__ == '__main__':
    app.run(debug=True)