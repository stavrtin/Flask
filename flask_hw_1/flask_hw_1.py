from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html')


@app.route('/clothing/')
def clothing():
    cloth = [
        {'name': 'Футболка',
         'color': 'Белый',
         'size': 50,
         'price': 3010},
        {'name': 'Штаны',
         'color': 'Синий',
         'size': 52,
         'price': 3020},
        {'name': 'Сорочка',
         'color': 'Белый',
         'size': 56,
         'price': 3030},
        {'name': 'Брюки',
         'color': 'Красный',
         'size': 45,
         'price': 3500},
    ]
    barahlo = {'shmotki': cloth}

    return render_template('clothing.html', **barahlo)


@app.route('/shoes/')
def shoes():
    shuz = [
        {'name': 'Тапки',
         'color': 'Белый',
         'size': 42,
         'price': 2220},
        {'name': 'Босоножки',
         'color': 'Синий',
         'size': 36,
         'price': 311020},

    ]
    barahlo = {'shmotki': shuz}
    return render_template('shoes.html', **barahlo)



@app.route('/jackets/')
def jackets():
    jack = [
        {'name': 'Косуха',
         'color': 'Белый',
         'size': 42,
         'price': 2220},
        {'name': 'Кожанка',
         'color': 'Синий',
         'size': 36,
         'price': 3333},
]
    barahlo = {'shmotki': jack}
    return render_template('jackets.html', **barahlo)


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)
