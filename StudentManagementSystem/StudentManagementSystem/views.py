"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template , request , redirect , url_for
from flask_sqlalchemy import SQLAlchemy
from StudentManagementSystem import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable = False) #nullable  = False meaning no values cannot be stored , if user enters nothing it is not stored
    age = db.Column(db.Integer,nullable = False)


@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students = students)


@app.route('/add',methods = ['GET','POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        
        student = Student(name = name , age = age)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')
