#!/usr/bin/env python3

from flask import Blueprint, request, jsonify
from app.database.db import db
from app.models.models import *

person_routes = Blueprint('api', __name__)

@person_routes.route('/api', methods=['POST'])
def create_person():
    try:
        name = request.json['name']

        # Validate if name is string
        if not isinstance(name, str):
            return jsonify({'error': 'Name must be a string'}), 400

        new_person = Person(name=name)
        db.session.add(new_person)
        db.session.commit()

        return person_schema.jsonify(new_person), 201

    except KeyError:
        return jsonify({'error': 'Name fiels is empty'}), 400

    except ValidationError as e:
        return jsonify({'error': e.messages}), 400

@person_routes.route('/api/<int:person_id>', methods=['GET'])
def get_person_by_id(person_id):
    try:
        # Attempt to convert 'person_id' to an integer
        person_id = int(person_id)

        # Check if 'person_id' is a positive integer
        if person_id <= 0:
            return jsonify({'error': 'Person ID must be a positive integer e.g., 1'}), 400

        # Check for specified id
        person = Person.query.get(person_id)

        if person is None:
            return jsonify({'error': 'Person not found'}), 404

        return person_schema.jsonify(person)

    except ValueError:
        return jsonify({'error': 'Invalid id format'}), 400



@person_routes.route('/api/<string:name>', methods=['GET'])
def get_person_by_name(name):
    try:
        # Check if name is a string
        if not isinstance(name, str):
            return jsonify({'error': 'Name must be a string'}), 400

        # Query the Person table by 'name' field
        person = Person.query.filter_by(name=name).first()

        if person is None:
            return jsonify({'error': 'Person not found'}), 404

        return person_schema.jsonify(person)

    except ValueError:
        return jsonify({'error': 'Invalid name format'}), 400

@person_routes.route('/api/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    try:
        # Check if 'person_id' is an integer
        if not isinstance(person_id, int):
            return jsonify({'error': 'Person ID must be an integer'}), 400

        person = Person.query.get(person_id)

        if person is None:
            return jsonify({'error': 'Person not found'}), 404

        # Update the person's name
        person.name = request.json['name']
        db.session.commit()

        return person_schema.jsonify(person)

    except ValueError:
        return jsonify({'error': 'Invalid id format'}), 400

    except KeyError:
        return jsonify({'error': 'Name field is empty'}), 400

    except ValidationError as e:
        return jsonify({'error': e.messages}), 400

@person_routes.route('/api/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    try:
        # Check if 'person_id' is an integer
        if not isinstance(person_id,int):
            return jsonify({'error': 'Person ID must be an integer e.g 1'}), 400

        # Check for specified id
        person = Person.query.get(person_id)

        if person is None:
            return jsonify({'error': 'Person not found'}), 404
       
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person deleted successfully'})

    except ValueError:
        return jsonify({'error': 'Invalid id format'}), 400

@person_routes.route('/api/<string:name>', methods=['DELETE'])
def delete_person_by_name(name):
    try:
        # Check if name is a string
        if not isinstance(name, str):
            return jsonify({'error': 'Name must be a string'}), 400

        # Query the Person table by 'name' field
        person = Person.query.filter_by(name=name).first()

        if person is None:
            return jsonify({'error': 'Person not found'}), 404

        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person deleted successfully'})

    except ValueError:
        return jsonify({'error': 'Invalid name format'}), 400

