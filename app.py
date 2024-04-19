import os
# import things that I can use html
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import first_code

app = Flask(__name__)

# import the module
import sqlite3

# make a  connection object
connection_obj = sqlite3.connect('project.sqlite')

# make a cursor object
cursor_obj = connection_obj.cursor()

def main():
    try:        
        # creating tables if it doesn't exit
        # cursor_obj.execute('drop table students')
        students_table = '''CREATE TABLE if not exists STUDENTS
                            (StudentID integer primary key autoincrement,
                            FirstName varchar(20),
                            LastName varchar(30),
                            Grade integer);'''

        cursor_obj.execute(students_table)
        temp = cursor_obj.execute('select avg(Grade) from students;')

    except Exception as e:
        print(e.message)

    # close the object at the end
    connection_obj.close()    

if __name__ == "__main__":
    main()

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'project.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
project = SQLAlchemy(app)

class Students(project.Model):
    StudentID = project.Column(project.Integer, primary_key=True)
    FirstName = project.Column(project.String(20))
    LastName = project.Column(project.String(30))
    Grade = project.Column(project.Integer)

    def __repr__(self):
        return f'<Student {self.StudentID}-{self.FirstName}-{self.LastName}-{self.Grade}'

@app.get("/")
def home():
    grade_list = []
    grade_list = project.session.query(Students).all()
    return render_template('base.html', grade_list=grade_list)

@app.post("/add")
def add():
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    grd = request.form.get("grd")
    new_student = Students(FirstName=fname, LastName=lname, Grade=grd)
    project.session.add(new_student)
    project.session.commit()
    return redirect(url_for("home"))

@app.get("/delete/<int:student_id>")
def delete(student_id):
    stu = project.session.query(Students).filter_by(StudentID= student_id)
    project.session.delete(stu)
    project.session.commit()
    return redirect(url_for("home"))


@app.get("/get_average/")
def average():
    project.session.update()
    project.session.commit()
    return redirect(url_for("home"))
