
# Person API Documentation

Welcome to the documentation for the Person API. This API allows you to perform CRUD (Create, Read, Update, Delete) operations on the "person" resource.

## Table of Contents

1. [Setup Instructions](#setup-instructions)
2. [Endpoints](#endpoints)
   - [Create a Person](#create-a-person)
   - [Get All Persons](#get-all-persons)
   - [Get Person by ID](#get-person-by-id)
   - [Get Person by Name](#get-person-by-name)
   - [Update Person by ID](#update-person-by-id)
   - [Delete Person by ID](#delete-person-by-id)
3. [Sample API Usage](#sample-api-usage)

## Setup Instructions

To run this API on your local machine, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/kevinkoech357/stage_two_backend.git
   cd stage_two_backend
```
2.  Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: env\Scripts\activate
```
3.  Install the required dependencies:
```bash
pip install -r requirements.txt
```
4.  Start the API:
```bash
python3 run.py
or
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```
The API should now be accessible at http://localhost:5000.

## Endpoints
### Create a Person

    URL: /api
    Method: POST
    Request Body: JSON object with person details.

    ```json
    {
      "name": "John Doe"
    }
    ```
    ```json
    {
        "name": "Jane Doe"
    }
    ```
    Response:
        Status Code: 201 Created
        Body: {"message": "Person created successfully"}
### Get All Persons

    URL: /api/all
    Method: GET
    Response:
        Status Code: 200 OK
        Body: List of persons.

    ```json

    [
      {
        "id": 1,
        "name": "John Doe"
      },
      {
        "id": 2,
        "name": "Jane Doe"
      }
    ]

### Get Person by ID

    URL: /api/{person_id} e.g /api/1
    Method: GET
    Response:
        Status Code: 200 OK
        Body: Person details.

    ```json
    {
      "id": 1,
      "name": "John Doe",
    }

### Get Person by Name

    URL: /persons/{name} e.g /api/John Doe
    Method: GET
    Response:
        Status Code: 200 OK
        Body: List of persons with the given name.

    ```json
    {
        "id": 1,
        "name": "John Doe",
    }
    ```
### Update Person by ID

    URL: /persons/{person_id}
    Method: PUT
    Request Body: JSON object with fields to update (e.g., "name")

    ```json
    {
      "name": "Updated Name"
    }
    ```
    Response:
        Status Code: 200 OK
        Body: {"message": "Person updated successfully"}

### Delete Person by ID

    URL: /persons/{person_id}
    Method: DELETE
    Response:
        Status Code: 200 OK
        Body: {"message": "Person deleted successfully"}

## Sample API Usage

Here are some sample API requests using the curl command:

#### Create a new person:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Kevin Koech}' http://localhost:5000/api
```
#### Get all persons:
```bash
curl http://localhost:5000/api
```
#### Get a person by ID:
```bash
curl http://localhost:5000/api/1
```
#### Update a person by ID:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name"}' http://localhost:5000/api/1
```
#### Delete a person by ID:
```bash
curl -X DELETE http://localhost:5000/api/1
```
