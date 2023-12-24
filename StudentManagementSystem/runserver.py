"""
This script runs the StudentManagementSystem application using a development server.
"""

from os import environ
from StudentManagementSystem import app
from StudentManagementSystem.views import db

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    with app.app_context():
        db.create_all()
    app.run(HOST, PORT,debug = True)
