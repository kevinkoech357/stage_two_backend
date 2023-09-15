# API DOCUMENTATION

## Introduction
This repository hosts a REST API built using flask framework and sqlite as the database. It allows the user to perform different CRUD operations on a person resource, specifically name. Navigate to different directories to see the code:

```bash
(env) kevinkoech357@kevinkoech:~/Personal/HNGx/stage_two_backend$ tree -L 2
.
├── app
│   ├── database
│   ├── __init__.py
│   ├── models
│   ├── __pycache__
│   └── routes
├── docs
│   └── DOCUMENTATION.md
├── instance
│   └── test.db
├── __pycache__
│   └── run.cpython-311.pyc
├── README.md
├── requirements.txt
└── run.py
```

## Usage
### Cloning repository
```bash
git clone https://github.com/kevinkoech357/stage_two_backend
cd stage_two_backend
```
### Creating virutalenv
```bash
python3 -m venv env
source env/bin/activate
```
### Installing dependencies
```bash
pip install -r requirements.txt
```
### Starting server
```bash
gunicorn -w 4 run:app
```

## Testing
### Using curl
#### Create a new person:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe"}' http://localhost:8000/api
```
#### Retrieve details of a person by ID:
```bash
curl http://localhost:8000/api/1
```
#### Retrieve all persons
```bash
curl -X GET http://localhost:8000/api/all
```
#### Update the details of an existing person:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name"}' http://localhost:8000/api/1
```
#### Remove a person by ID:
```bash
curl -X DELETE http://localhost:8000/api/1
```
### Using Postman
Visit ```https://www.postman.com/kevinkoech357/workspace/hng-stage-two-internship/collection/29637783-a59d3879-5053-4704-958e-d97db1f62021?action=share&creator=29637783``` to check collection and add more tests.

### UML Diagram
Navigate to docs and open uml_diagram or click ```https://github.com/kevinkoech357/stage_two_backend/blob/main/docs/uml_diagram```
