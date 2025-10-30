# Todo App

A comprehensive Django-based Todo application that allows users to manage their tasks efficiently. This project includes user authentication, task creation, updating, deletion, completion tracking, and a history feature for deleted tasks.

## Features

- **User Authentication**: Secure registration, login, logout, and profile management with password change functionality.
- **Task Management**: Add, update, delete, and search tasks.
- **Task Completion**: Mark tasks as complete or incomplete, with separate views for completed tasks.
- **History Tracking**: Deleted tasks are stored in a history model, allowing users to restore them if needed.
- **Search Functionality**: Search tasks by title or description.
- **Support Form**: Contact form for user support.
- **Responsive Design**: Clean and simple UI using HTML and CSS.

## Technologies Used

- **Backend**: Django 5.2.6
- **Database**: SQLite (default Django database)
- **Frontend**: HTML, CSS (with Django templates)
- **Authentication**: Django's built-in authentication system
- **Other**: Python 3.x

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/todo-app.git
   cd todo-app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   The project uses Django. If `requirements.txt` is not present or empty, install Django manually:
   ```bash
   pip install django
   ```
   Or if you have a `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

1. **Register**: Create a new account at `/register/`.
2. **Login**: Log in with your credentials at `/login/`.
3. **Home**: View your active tasks, search, and manage them.
4. **Add Task**: Click "Add Task" to create a new task.
5. **Update Task**: Edit existing tasks.
6. **Delete Task**: Delete tasks (they move to history).
7. **Completed Tasks**: View and manage completed tasks.
8. **History**: View deleted tasks and restore them.
9. **Profile**: Update your profile information.
10. **Change Password**: Change your password securely.
11. **Support**: Use the support form to contact administrators.

## Project Structure

```
todo_project/
├── todo/                 # Main Django project
│   ├── settings.py       # Project settings
│   ├── urls.py           # Main URL configuration
│   └── ...
├── base/                 # Main app for task management
│   ├── models.py         # TaskModel, HistoryModel
│   ├── views.py          # Views for tasks, history, etc.
│   ├── templates/        # HTML templates
│   └── ...
├── user_auth/            # App for user authentication
│   ├── views.py          # Login, register, profile views
│   ├── templates/        # Auth-related templates
│   └── ...
├── static/               # Static files (CSS)
├── templates/            # Base templates
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
└── README.md             # This file
```

## Database Models

- **TaskModel**: Stores task details (title, description, user, completion status).
- **HistoryModel**: Stores deleted tasks for restoration (title, description, user, original ID).

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please use the in-app support form or contact the maintainers.

---

*Note: This README assumes standard Django setup. Adjust paths and commands as needed for your environment.*
