#!/usr/bin/env python3

from flask import request, jsonify
from app.database.db import db

@app.route('/api', methods=['POST'])
def create_person():
    name = request.json['name']
    age = request.json.get('age')
    new_person = Person(name=name)
    db.session.add(new_person)
    db.session.commit()
    return person_schema.jsonify(new_person)

@app.route('/api/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = Person.query.get(person_id)
    return person_schema.jsonify(person)

@app.route('/api/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    person = Person.query.get(person_id)
    person.name = request.json['name']
    db.session.commit()
    return person_schema.jsonify(person)

@app.route('/api/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = Person.query.get(person_id)
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully'})


