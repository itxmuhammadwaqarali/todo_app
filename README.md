# Todo App API

A feature-rich **Todo API** built with **FastAPI**.
Users can register, log in, and manage their todos with **priority, due dates, completion status, search, and stats**.

---

## Features

* User Registration & Login (JWT Auth)
* Create Todo with **priority** and optional **due date**
* Get all Todos & single Todo
* Update Todo (title, task, priority, due date, completed)
* Toggle completion status
* Delete Todo
* Search Todos by title, task, priority, or completion status
* View Todo Stats: total, completed, pending
* Automatically stores **creation date**

---

## Tech Stack

* Python 3
* FastAPI
* SQLAlchemy
* SQLite
* JWT Authentication
* Pydantic Schemas

---

## Installation & Run

```bash
# Clone repo
git clone https://github.com/itxmuhammadwaqarali/todo_app.git
cd todo_app

# Activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux / Mac
# venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload
```

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

## API Docs

Swagger UI:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

ReDoc:

[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---


* Todo List with priorities
* Search & filter results
* Stats endpoint showing total/completed/pending

---
