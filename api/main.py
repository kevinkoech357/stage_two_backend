#!/usr/bin/env python3

'''
This module initializes the api and contains all
methods for performing CRUD operations.
HTTP methods used: GET, POST, PUT, DELETE
'''

# Importing
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


# Initializing api
app = Flask(__name__)

# Configuring database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

# Initialize SQLAlchemy
db = SQLAlchemy(app)

class Person(db.Model):
    '''
    This class contains name, which is a string,
    resource of Person.
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, name):
        '''
        This method initializes name attribute
        of Person object.
        '''
        self.name = name

    def __str__(self):

        return self.name


class PersonSchema(SQLAlchemySchema):

    class Meta:

        model = Person
        load_instance = True

    id = auto_field()
    name = auto_field()


@app.route('/api', methods = ['POST'])
def create_person():

    data = request.get_json()
    person_schema = PersonSchema()
    person, error = person_schema.load(data)
    result = person_schema.dump(person.create()).data
    return make_response(jsonify({"person": result}))


if __name__ == '__main__':
    # Create database with all tables specified
    with app.app_context():
        db.create_all()
    print('Database created successfully!')
    app.run(debug=True)
