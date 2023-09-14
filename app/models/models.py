#!/usr/bin/env python3

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.database.db import db

ma = Marshmallow()

class Person(db.Model):
    '''
    This class contains name, which is a string,
    resource of Person.
    '''
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        '''
        This method initializes name attribute
        of Person object.
        '''
        self.name = name

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __str__(self):
        return self.name


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        fields = ('id', 'name')

person_schema = PersonSchema()
people_schema = PersonSchema(many=True)

