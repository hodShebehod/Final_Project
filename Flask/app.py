import os
# import things that I can use html
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)

'''@app.get("/")
def home():
    return 'Hello, World!'

@app.get("/bye")
def bye():
    return 'Bye, World!'    '''

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'project.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
project = SQLAlchemy(app)

class Student(project.Model):
    StudentID = project.Column(project.Integer, primary_key=True)
    FirstName = project.Column(project.String(20))
    LastName = project.Column(project.String(30))
    Grade = project.Column(project.Integer)

    def __repr__(self):
        return f'<Student {self.StudentID}-{self.FirstName}-{self.LastName}'

@appeccc.get("/")
def home():
    grade_list = project.session.query(STUDENTS).all()
    return render_template("base.html", grade_list=grade_list)

@app.post("/add")
def add():
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    grd = request.form.get("grd")
    new_student = Student(FirstName=fname, LastName=lname, Grade=grd)
    project.session.add(new_student)
    project.session.commit()
    return redirect(url_for("home"))

@app.get("/update/<int:student_id>")
def update():
    stu = project.session.query(STUDENTS).filter(Student.StudentID == student_id)
    stu.FirstName = request.form.get("fname")
    stu.LastName = request.form.get("lname")
    stu.Grade = request.form.get("grd")
    project.session.commit()
    return redirect(url_for("home"))

@app.get("/delete/<int:student_id>")
def delete():
    stu = project.session.query(STUDENTS).filter(Student.StudentID == student_id)
    project.session.delete(stu)
    project.session.commit()
    return redirect(url_for("home"))
