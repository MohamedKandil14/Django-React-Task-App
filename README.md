# Django Task Management API

## Description

This project is a simple Task Management API built with Django and Django REST Framework. It allows users to create, retrieve, update, and delete their tasks, incorporating a secure token-based authentication system.

## Features

* **Task Management:**
    * Create new tasks (title, description, completion status).
    * Retrieve all tasks for the current authenticated user.
    * Retrieve details of a specific task.
    * Update an existing task.
    * Delete a task.
* **Authentication & Authorization:**
    * User login to obtain an authentication token.
    * Protection of task endpoints, allowing access only to authenticated users.
    * Each task is linked to its owner (the user who created it).
    * Users can only view, modify, or delete their own tasks.

## Requirements

Ensure you have the following installed on your system:

* Python 3.8+
* pip (Python package installer)
* Git (for cloning the repository)

2. Setup Virtual Environment
It is highly recommended to use a virtual environment to isolate project dependencies:

Bash

python -m venv venv
# On Windows, activate the virtual environment:
venv\Scripts\activate
# On macOS/Linux, activate the virtual environment:
source venv/bin/activate
3. Install Dependencies
Install all required libraries from the requirements.txt file:

Bash

pip install -r requirements.txt
4. Configure Environment Variables (.env file)
Create a .env file in the same directory as manage.py to store your Django SECRET_KEY. This file will NOT be committed to Git for security reasons.

Bash

touch .env
Open the .env file and add the following line. You can generate a new secret key using an online Django secret key generator or keep a temporary value for development:

SECRET_KEY=your_very_long_and_complex_secret_key_here
5. Database Setup
Run the migrations to create the database tables:

Bash

python manage.py makemigrations tasks
python manage.py migrate
If prompted to provide a one-off default value for the owner_id column during makemigrations (especially if you had existing data), enter 1 (typically, the first user ID is for the superuser you create).

6. Create Superuser
To access the Django Admin panel and create users for testing:

Bash

python manage.py createsuperuser
Follow the prompts to enter a username, email, and password.

7. Run the Server
Now you can start the Django development server:

Bash

python manage.py runserver
The API will be available at http://127.0.0.1:8000/.

API Endpoints
Below are the main API endpoints and how to interact with them:

Base API URL: http://127.0.0.1:8000/api/

1. User Login
URL: /api/login/
Method: POST
Description: Authenticates a user and returns an authentication token.
Body (JSON):
JSON

{
    "username": "your_username",
    "password": "your_password"
}
Successful Response (200 OK - JSON):
JSON

{
    "token": "a_very_long_random_string_representing_your_auth_token"
}
2. Task Management
Note: All task-related requests require an Authorization Header with the token obtained from login.

Required Header:
Key: Authorization
Value: Token YOUR_AUTH_TOKEN_HERE (Replace YOUR_AUTH_TOKEN_HERE with the actual token, with a single space after the word Token).
2.1. List & Create Tasks
URL: /api/tasks/
Method:
GET: To retrieve all tasks for the current authenticated user.
Successful Response (200 OK - JSON): A list of tasks.
JSON

[
    {
        "id": 1,
        "owner": 1,
        "title": "Buy Groceries",
        "description": "Milk, bread, eggs, fruit.",
        "completed": false,
        "created_at": "2025-06-11T14:30:00Z"
    },
    {
        "id": 2,
        "owner": 1,
        "title": "Prepare Presentation",
        "description": "Review slides, add charts.",
        "completed": true,
        "created_at": "2025-06-10T09:00:00Z"
    }
]
POST: To create a new task.
Body (JSON):
JSON

{
    "title": "New Task Title",
    "description": "Detailed description for the new task.",
    "completed": false
}
Successful Response (201 Created - JSON): Details of the newly created task.
JSON

{
    "id": 3,
    "owner": 1, # Will be automatically assigned based on the authenticated user
    "title": "New Task Title",
    "description": "Detailed description for the new task.",
    "completed": false,
    "created_at": "2025-06-11T14:45:00Z"
}
2.2. Retrieve, Update & Delete Task
URL: /api/tasks/<id>/ (Replace <id> with the task's ID)
Method:
GET: To retrieve details of a specific task.
Successful Response (200 OK - JSON): Task details.
PUT: To update all fields of a task.
Body (JSON):
JSON

{
    "title": "Updated Task Title",
    "description": "New and detailed description.",
    "completed": true
}
Successful Response (200 OK - JSON): Updated task details.
PATCH: To partially update specific fields of a task.
Body (JSON):
JSON

{
    "completed": true
}
Successful Response (200 OK - JSON): Updated task details.
DELETE: To delete a task.
Successful Response (204 No Content).
Contributing
Contributions are welcome! If you'd like to improve this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature-name).
Make your changes and commit them (git commit -m 'Add new feature').
Push to your branch (git push origin feature/your-feature-name).
Open a Pull Request.