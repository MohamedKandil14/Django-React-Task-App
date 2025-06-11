# Task Management Fullstack Application

This is a fullstack task management application built with Django Rest Framework for the backend and React.js for the frontend. Users can register, log in, create, view, update, and delete their tasks.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

* User Registration and Login (Token-based authentication)
* Create, Read, Update, Delete (CRUD) tasks
* Tasks are linked to specific users (users can only manage their own tasks)
* Mark tasks as completed/uncompleted
* Modern and responsive UI with Material-UI
* Toast notifications for user feedback
* Filtering, searching, and ordering of tasks (Backend capability)

## Technologies Used

**Backend:**
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework (DRF)](https://www.django-rest-framework.org/)
* [SQLite](https://www.sqlite.org/index.html) (Default database, can be changed)
* [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) (If you used JWT for login instead of TokenAuthentication. If you use TokenAuth, you can remove this.)
* [django-filter](https://django-filter.readthedocs.io/en/stable/) (For filtering tasks)

**Frontend:**
* [React.js](https://react.dev/)
* [Create React App](https://create-react-app.dev/)
* [Material-UI (MUI)](https://mui.com/)
* [React Router DOM](https://reactrouter.com/en/main)
* [Axios](https://axios-http.com/)
* [React Toastify](https://fkhadra.github.io/react-toastify/)

## Project Structure
├── my_task_api/           # Django Backend (REST API)
│   ├── my_task_api/       # Main Django project settings
│   ├── tasks/             # Django app for task management
│   ├── manage.py
│   └── ...
├── task-frontend/         # React Frontend application
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.js, index.js, etc.
│   └── ...
├── .gitignore             # Git ignore file for the root directory
└── README.md
## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* **Node.js & npm (or Yarn):** For the React frontend.
    * [Download Node.js](https://nodejs.org/en/download/)
* **Python 3.x & pip:** For the Django backend.
    * [Download Python](https://www.python.org/downloads/)
* **Git:** For cloning the repository.
    * [Download Git](https://git-scm.com/downloads)

### Backend Setup (`my_task_api`)

1.  **Navigate to the backend directory:**
    ```bash
    cd my_task_api
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
        python -m venv venv
```

3.  **Activate the virtual environment:**
    * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Django and other dependencies:**
    ```bash
    pip install Django djangorestframework djangorestframework-simplejwt django-filter django-cors-headers
    # Note: adjust the above pip install command based on your actual pip freeze output or requirements.txt
    ```
    *(**Pro Tip:** It's good practice to create a `requirements.txt` file after installing dependencies: `pip freeze > requirements.txt`. Then users can just do `pip install -r requirements.txt`)*

5.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser** (optional, for admin access):
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the Django development server:**
    ```bash
    python manage.py runserver
    ```
    The backend API will be running at `http://127.0.0.1:8000/`.

### Frontend Setup (`task-frontend`)

1.  **Open a new terminal window.**
2.  **Navigate to the frontend directory:**
    ```bash
    cd task-frontend
    ```

3.  **Install Node.js dependencies:**
    ```bash
    npm install
    # or
    # yarn install
    ```

4.  **Start the React development server:**
    ```bash
    npm start
    # or
    # yarn start
    ```
    The React application will open in your browser, usually at `http://localhost:3000/`.

## Usage

1.  **Register a new user** on the signup page (`/signup`).
2.  **Log in** with your new credentials on the login page (`/login`).
3.  Once logged in, you will be redirected to the **tasks dashboard** where you can:
    * Create new tasks.
    * View your existing tasks.
    * Mark tasks as complete or incomplete.
    * Delete tasks.
4.  You can log out using the "Logout" button.

## API Endpoints

*(This section assumes your API URLs are configured as discussed)*

**Authentication:**
* `POST /api/register/` - Register a new user.
    * **Request Body:** `{"username": "your_username", "password": "your_password"}`
    * **Response:** `{"user": {...}, "token": "your_auth_token"}`
* `POST /api/login/` - Authenticate a user and get an auth token.
    * **Request Body:** `{"username": "your_username", "password": "your_password"}`
    * **Response:** `{"token": "your_auth_token"}`

**Tasks:**
* `GET /api/tasks/` - List all tasks for the authenticated user.
    * **Authentication:** Token (in `Authorization` header: `Token your_auth_token`)
    * **Query Params (optional):**
        * `?completed=true` / `?completed=false`
        * `?search=keyword`
        * `?ordering=created_at` / `?ordering=-created_at` (for descending)
* `POST /api/tasks/` - Create a new task.
    * **Authentication:** Token
    * **Request Body:** `{"title": "New Task", "description": "Details about the task"}`
* `GET /api/tasks/<id>/` - Retrieve a specific task.
    * **Authentication:** Token
* `PATCH /api/tasks/<id>/` - Partially update a task.
    * **Authentication:** Token
    * **Request Body:** `{"completed": true}` or `{"title": "Updated Title"}`
* `DELETE /api/tasks/<id>/` - Delete a task.
    * **Authentication:** Token

## Screenshots

*(Optional: Add screenshots of your application here. You can drag and drop images directly into the Markdown file on GitHub or use image hosting services.)*

![Login Page Screenshot](path/to/your/login-screenshot.png)
![Tasks Page Screenshot](path/to/your/tasks-screenshot.png)

