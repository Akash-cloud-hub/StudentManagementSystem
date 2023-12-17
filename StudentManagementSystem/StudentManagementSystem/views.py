"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from StudentManagementSystem import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

db = SQLAlchemy(app)

#class Student(db.Model):
  