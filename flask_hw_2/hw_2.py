from flask import Flask, render_template, redirect, url_for, request, make_response, session
import ast


app = Flask(__name__)

@app.route('/')
def main():
    # устанавливаем cookie
    response = make_response("Cookie установлен")
    response.set_cookie('username', 'admin')
    # return response
    return render_template('index_hw2.html')

@app.route('/input_form', methods=['GET', 'POST'])
def input_form():
    if request.method == 'POST':
        user_name = (request.form.get('name'))
        user_mail = (request.form.get('email'))
        data = {"user_name": user_name,
                "user_mail": user_mail}
        return redirect(url_for('df_greeting', data=data))
    return render_template('users_data.html')

@app.route('/df_greeting/<data>')
def df_greeting(data):
    context = ast.literal_eval(data)
    # cockies


    return render_template('greeting.html', **context)


@app.route('/logout/')
def logout():
    session.pop('user_name', None)
    return redirect(url_for('input_form'))



if __name__ == '__main__':
    app.run(debug=True)