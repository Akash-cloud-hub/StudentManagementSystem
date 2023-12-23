"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
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

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)