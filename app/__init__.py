#!/usr/bin/env python3

from flask import Flask, request, jsonify
from app.database.db import db
from app.models import *
from app.routes import *

DB_NAME = 'test.db'

app = Flask(__name__)
app.config["SECRET_KEY"] = "notasecret iguess"
# configure database location, will be in app directory
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
# initiliaze database
db.init_app(app)

def create_database(app):
    # Create database with all tables specified
    with app.app_context():
        db.create_all()
    print('Database created successfully!')

if __name__ == '__main__':
    create_database(app)

    app.run(debug=True)


