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

    def __repr__(self):
        return f'<Student {self.StudentID}-{self.FirstName}-{self.LastName}'

@app.get("/")
def home():
    grade_list = project.session.query(Student).all()
    return render_template("base.html", grade_list=grade_list)