#!/usr/bin/env python3

from flask import Flask
from app.database.db import db

DB_NAME = 'test.db'

def start_app():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "notasecret iguess"
    # configure database location, will be in app directory
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initiliaze database
    db.init_app(app)

    from app.models.models import Person, PersonSchema
    from app.routes.person_routes import person_routes

    app.register_blueprint(person_routes)

    create_database(app)

    return app

def create_database(app):
    # Create database with all tables specified
    with app.app_context():
        db.create_all()
    print('Database created successfully!')

