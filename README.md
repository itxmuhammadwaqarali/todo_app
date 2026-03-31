# Todo App

A full-stack **Todo Application** with a **FastAPI** backend and **React** frontend.
Users can register, log in, and manage their todos with **priority, due dates, completion status, search, and stats**.

Built with modern technologies for a seamless user experience.

---

## Features

### Backend (FastAPI)
* User Registration & Login (JWT Auth with HTTPBearer)
* Create Todo with **priority** and optional **due date**
* Get all Todos & single Todo
* Update Todo (title, task, priority, due date, completed)
* Toggle completion status
* Delete Todo
* Search Todos by title, task, priority, or completion status
* View Todo Stats: total, completed, pending
* Automatically stores **creation date**

### Frontend (React + Vite)
* User authentication (Login & Register)
* Dashboard with todo management
* Real-time todo list updates
* Mark tasks as complete/incomplete
* Delete tasks
* Filter todos (All, Completed, Pending, High Priority)

---

## Tech Stack

### Backend
* Python 3
* FastAPI
* SQLAlchemy
* SQLite / PostgreSQL
* JWT Authentication (HTTPBearer)
* Pydantic Schemas
* Alembic Migrations

### Frontend
* React 19
* Vite
* React Router v7
* Axios
* CSS3 (Custom Styling)

---

## Installation & Setup

### Backend Setup

```bash
# Navigate to project directory
cd todo_app

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux / Mac
# venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn app.main:app --reload
```

The backend will be available at: **http://127.0.0.1:8000**

### Frontend Setup

```bash
# Navigate to frontend directory
cd todo_app/todo-frontend

# Install dependencies
npm install

# Run the development server
npm run dev
```

The frontend will be available at: **http://localhost:5173**

### Access the Application

* **Frontend**: [http://localhost:5173](http://localhost:5173)
* **API Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

| Method | Endpoint                  | Description                                  |
| ------ | ------------------------- | -------------------------------------------- |
| POST   | `/register`               | Register a new user                          |
| POST   | `/login`                  | Login & get JWT token                        |
| POST   | `/todos`                  | Create a new todo                            |
| GET    | `/todos`                  | Get all todos                                |
| PATCH  | `/todos/{todo_id}`        | Update a todo                                |
| PATCH  | `/todos/{todo_id}/toggle` | Toggle completion status                     |
| DELETE | `/todos/{todo_id}`        | Delete a todo                                |
| GET    | `/todos/search`           | Search todos (title/task/priority/completed) |
| GET    | `/todos/stats`            | Get todo stats (total, completed, pending)   |

---

## Example Requests

**Create Todo**

```json
{
  "title": "Finish FastAPI project",
  "task": "Add search and stats endpoints",
  "priority": "high",
  "due_date": "2026-04-01T23:59:00"
}
```

**Response**

```json
{
  "id": "uuid",
  "title": "Finish FastAPI project",
  "task": "Add search and stats endpoints",
  "completed": false,
  "priority": "high",
  "created_at": "2026-03-26T15:30:00",
  "due_date": "2026-04-01T23:59:00"
}
```

---

## Project Structure

```
todo_app/
├── app/                    # FastAPI backend
│   ├── core/              # Authentication logic
│   ├── api/               # API routes and dependencies
│   ├── crud/              # Database operations
│   ├── models/            # SQLAlchemy models
│   ├── schemas/           # Pydantic schemas
│   ├── database.py        # Database configuration
│   └── main.py            # FastAPI application
├── alembic/               # Database migrations
├── todo-frontend/         # React frontend
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Page components
│   │   ├── context/       # React context (Auth)
│   │   ├── api/           # API client
│   │   └── App.jsx        # Main App component
│   ├── package.json       # Frontend dependencies
│   └── vite.config.js     # Vite configuration
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

---

## Frontend Features Explained

### Authentication
* **Login Page**: Users can login with username and password
* **Register Page**: New users can create an account
* **Protected Routes**: Dashboard is only accessible to authenticated users
* **Token Storage**: JWT tokens are stored in localStorage

### Todo Management
* **Create Todo**: Add new todos with title, description, priority, and due date
* **View Todos**: See all your todos in a clean list format
* **Update Todo**: Mark todos as complete/incomplete
* **Delete Todo**: Remove todos permanently
* **Filter Todos**: Filter by status (All, Completed, Pending, High Priority)
