from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from task3.model_mark import db, Student, Faculty, Subject, StudentSubject
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_stud_mark.db'
db.init_app(app)

# ---------------- создаем БД по моделям, сформированным в файле МОДЕЛЬ.ру ----------
@app.cli.command('init-db-mark')
def int_db_mark():
    db.create_all()
    print('Ну поехали!!!')


@app.cli.command('add-fac')
def add_fac():
    fac_list = ['Механ','Физтех','Биологический','Математический','АСУ']
    decans_list = ['Шпунтик','Винтиков','Пауков','Гринблат','Горчаков']
    for i in fac_list:
        db.session.add(Faculty(
            faculty_name=i,
        decan=decans_list[fac_list.index(i)]))
    db.session.commit()
    print('Записи по факультетам созданы!!!')

@app.cli.command('add-stud')
def add_stud():
    stud_list = ['Иванов',
                 'Петров','Сидоров','Кусков','Тютчев',
                 'Петроввв','Ваидыоров','Рпвыусков','Тыфвютчев']
    for stud_i in stud_list:
        firstname = stud_i
        lastname = f'Петя_{random.randint(1,5)}'
        email = f'{firstname}@mail.ru'
        group = random.randint(1,5)
        id_faculty = random.choice([1,2,3,4,5])
        # for sub_ject in subj_list:
        db.session.add(Student(
            firstname=firstname,
            lastname=lastname,
            email=email,
            group=group,
            id_faculty=id_faculty,
        ))
    db.session.commit()
    print('Записи по студентам  созданы!!!')


@app.cli.command('add-subjects')
def add_fac():
    subj_list = ['Математика','Русский','Физика','Информатика','Сопромат']
    for i in subj_list:
        db.session.add(Subject(subject_name=i))
    db.session.commit()
    print('Записи по ПРЕДМЕТАМ созданы!!!')

@app.cli.command('add-mark')
def add_fac():
    for student_id in range(1, 10):
        # -- количество предметов у студента ----
        count_subj = random.randint(1,5)
        for subject_id in range(1,count_subj + 1):
            db.session.add(StudentSubject(
                student_id=student_id,
                subject_id=subject_id,
                mark=random.randint(3,5),
            ))
    db.session.commit()
    print('Записи по ОЦЕНКАМ созданы!!!')


# ------------------
@app.route('/')
def start():
    return 'Подъем!!'


@app.route('/stud')
def stud():
    students = Student.query.all()
    content = {'students': students}
    return render_template('students_data.html', **content)

@app.route('/mark')
def mark():
    marks = StudentSubject.query.all()
    content = {'marks': marks}
    return render_template('students_data.html', **content)



if __name__ == '__main__':
    app.run(debug=True)