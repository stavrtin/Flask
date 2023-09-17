from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

'''
Задание №3
📌 Доработаем задача про студентов
📌 Создать базу данных для хранения информации о студентах и их оценках в учебном заведении. 
📌 База данных должна содержать две таблицы: "Студенты" и "Оценки". 
📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email. 
📌 В таблице "Оценки" должны быть следующие поля: id, id студента, название  предмета и оценка. 
📌 Необходимо создать связь между таблицами "Студенты" и "Оценки". 
📌 Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.'''


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    group = db.Column(db.String(120), nullable=False)
    id_faculty = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
    student_subjects = db.relationship(
        "StudentSubject", backref="student", lazy=True )

    def __repr__(self):
        return f'Student({self.firstname}, {self.email})'

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(80), unique=True, nullable=False)
    decan = db.Column(db.String(80), unique=True, nullable=False)
    students = db.relationship("Student", backref="faculty", lazy=True)

    def __repr__(self):
        return f'Faculty({self.faculty_name})'

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'Subject({self.subject_name})'


class StudentSubject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"))
    mark = db.Column(db.Integer, nullable=False)
    subject = db.relationship('Subject', backref=db.backref('students', lazy='dynamic'))

