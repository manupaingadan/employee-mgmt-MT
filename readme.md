# Employee Management System

A dynamic form–driven employee management platform built using Django, Django REST Framework, and jQuery.

## Features

### Authentication
- User registration
- Login using JWT
- Password change functionality
- User profile view and update

### Dynamic Forms
- Create form templates with multiple field types (text, number, date, password)
- Mark fields as required or optional
- Drag-and-drop field ordering
- Edit, view, and delete form templates

### Employee Management
- Create employees based on selected form templates
- List all employee records
- Filter/search employees using dynamic form fields
- View complete employee JSON data
- Delete employee records

### API Support
- Complete Postman collection provided
- All API endpoints documented
- JWT authentication integrated

## Project Setup

```bash
cd employee-mgmt
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser

python3 manage.py runserver
```

## API Endpoints

### Authentication

| Method | Endpoint                     | Description                         |
|--------|------------------------------|-------------------------------------|
| POST   | /api/auth/register/          | Register a new user                 |
| POST   | /api/auth/token/             | Obtain JWT access and refresh tokens|
| POST   | /api/auth/token/refresh/     | Refresh access token                |
| GET    | /api/auth/profile/           | Get logged-in user profile          |
| PATCH  | /api/auth/profile/            | Update user profile                 |
| POST   | /api/auth/change-password/    | Change user password                |

### Forms

| Method | Endpoint               | Description               |
|--------|------------------------|---------------------------|
| GET    | /api/forms/            | List all form templates   |
| POST   | /api/forms/            | Create a new form template|
| GET    | /api/forms/<id>/       | Retrieve a form           |
| PATCH  | /api/forms/<id>/       | Update a form             |
| DELETE | /api/forms/<id>/       | Delete a form             |

### Employees

| Method | Endpoint                                        | Description                    |
|--------|-------------------------------------------------|--------------------------------|
| GET    | /api/employees/                                 | List all employee records      |
| POST   | /api/employees/                                 | Create a new employee record   |
| GET    | /api/employees/<id>/                            | Retrieve employee details      |
| PATCH  | /api/employees/<id>/                            | Update employee record         |
| DELETE | /api/employees/<id>/                            | Delete employee record         |
| GET    | /api/employees/filter/?key=name&value=john      | Filter employees               |
