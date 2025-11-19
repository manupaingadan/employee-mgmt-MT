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

## Authentication
Method	Endpoint	                            Description
POST	/api/auth/register/	                    Register a new user
POST	/api/auth/token/	                    Login and obtain JWT access/refresh tokens
POST	/api/auth/token/refresh/	            Refresh access token
GET	/api/auth/profile/	                        Get logged-in user profile
PATCH	/api/auth/profile/	                    Update profile
POST	/api/auth/change-password/	            Change current user password

## Forms
Method	Endpoint	                            Description
GET	/api/forms/	                                List all form templates
POST	/api/forms/	                            Create a new form template
GET	/api/forms/<id>/	                        Retrieve a specific form
PATCH	/api/forms/<id>/	                    Update form
DELETE	/api/forms/<id>/	                    Delete form

## Employees
Method	Endpoint	                            Description
GET	/api/employees/	                            List all employee records
POST	/api/employees/	                        Create a new employee record
GET	/api/employees/<id>/	                    Retrieve employee details
PATCH	/api/employees/<id>/	                Update employee record
DELETE	/api/employees/<id>/	                Delete employee
GET	/api/employees/filter/?key=name&value=john	Filter employees by dynamic field