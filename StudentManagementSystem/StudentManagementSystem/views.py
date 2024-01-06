"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template , request , redirect , url_for
from flask_sqlalchemy import SQLAlchemy
from StudentManagementSystem import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

# servername = 'ABCIS-210013\SQLEXPRESS'
# dbname = 'Students'
# engine = create_engine('mssql+pyodbc://@' + servername + '/' + dbname + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')

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

@app.route('/edit/<int:id>',methods = ['GET','POST'])
def edit_studnet(id):
    students = Student.query.get(id)
    
    if request.method == 'POST':
        students.name = request.form['name']
        students.age = request.form['age']
        #no need to add it into the database again commit() will save the changes
        db.session.commit()        
        return redirect(url_for('index')) # 'index' calls for index()
    
    return render_template('edit.html',student = students)

@app.route('/delete/<int:id>',methods = ['GET'])
def delete_student(id):
    students = Student.query.get(id)
    db.session.delete(students)
    db.session.commit()
    return redirect(url_for('index'))
