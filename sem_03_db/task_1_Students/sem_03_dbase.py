from flask import Flask, render_template
from models import db, Student, Faculty # импорты прописываем !!!! относительно wsgi !!!!
from random import randint,choice

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_db_facultets.db'
db.init_app(app)

@app.route('/')
def start():
    return 'Поехали'

# ----------- создаем БД Студентов и записываем в нее данные --------
pass
# @app.cli.command('init-db')
# def init_db():
#     db.create_all()
#     print('ok')
#
#
# @app.cli.command('add-data-db')
# def add_sdudents():
#     for i in range(1,6):
#         fac = Faculty(fac_name=choice(['Мех','Жур','Биолог','Физ-тех','Филолог']))
#         db.session.add(fac)
#
#     for i in range(10):
#         stud = Student(firstname=f'Вася_{i}',
#                        lastname=f'lastname_{i}',
#                        age=randint(15,25),
#                        gender=choice(['м','ж']),
#                        group=randint(100,200),
#                        faculty_id=choice([1,2,3,4,5])
#                        )
#         db.session.add(stud)
#     db.session.commit()
#     print('ok - added')

# ----------- создаем БД и записываем в нее данные --------
pass
 # ----------- создаем БД Книги и записываем в нее данные --------
@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('ok')


@app.cli.command('add-data-db')
def add_sdudents():
    for i in range(1,6):
        fac = Faculty(fac_name=choice(['Мех','Жур','Биолог','Физ-тех','Филолог']))
        db.session.add(fac)

    for i in range(10):
        stud = Student(firstname=f'Вася_{i}',
                       lastname=f'lastname_{i}',
                       age=randint(15,25),
                       gender=choice(['м','ж']),
                       group=randint(100,200),
                       faculty_id=choice([1,2,3,4,5])
                       )
        db.session.add(stud)
    db.session.commit()
    print('ok - added')

# ----------- создаем БД и записываем в нее данные --------

@app.route('/students')
def all_students():
    student = Student.query.all()
    content = {'students': student}
    return render_template('students_data.html', **content)

if __name__ == '__main__':
    app.run(debug=True)
