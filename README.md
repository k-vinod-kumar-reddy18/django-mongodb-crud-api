# Django + MongoDB CRUD API

A backend project built using Django, Django REST Framework, PyMongo, and MongoDB.

## Project Overview

This project demonstrates how to build REST APIs using Django and connect them with MongoDB using PyMongo.

The project contains three modules:

- Students
- Student Profile
- Course

Each module supports CRUD operations.

The project also includes JWT-based authentication to protect the CRUD APIs.

## Technology Stack

- Python
- Django
- Django REST Framework
- MongoDB
- PyMongo
- Simple JWT
- DRF Spectacular
- Postman

## JWT Authentication

JWT authentication is implemented using Django REST Framework Simple JWT.

The authentication flow is:

```text
Username + Password
        ↓
      Login
        ↓
Access Token + Refresh Token
        ↓
Bearer Access Token
        ↓
Protected CRUD APIs

The CRUD APIs require a valid JWT Access Token.

API Modules
Students
POST   /students/create/
GET    /students/
GET    /students/{student_id}/
PUT    /students/{student_id}/update/
DELETE /students/{student_id}/delete/
Student Profile
POST   /student-profile/create/
GET    /student-profile/
GET    /student-profile/{student_id}/
PUT    /student-profile/{student_id}/update/
DELETE /student-profile/{student_id}/delete/
Course
POST   /courses/create/
GET    /courses/
GET    /courses/{course_id}/
PUT    /courses/{course_id}/update/
DELETE /courses/{course_id}/delete/
Authentication API
POST /login/

Login provides:

Access Token
Refresh Token

The Access Token is used to access the protected CRUD APIs.

Example:

Authorization: Bearer <access_token>
Project Structure
Django-MongoDB/

│
├── college_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── views.py
│   └── urls.py
│
├── student_profile/
│   ├── views.py
│   └── urls.py
│
├── course/
│   ├── views.py
│   └── urls.py
│
├── database.py
├── manage.py
├── requirements.txt
└── README.md