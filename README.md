# 🚀 FastAPI + SQLAlchemy + Alembic Todo Application

## Task Overview

This project is a complete backend system built using:

* FastAPI → API framework
* SQLAlchemy (ORM) → Database interaction
* Alembic → Database migrations
* SQLite → Local database

It follows a clean architecture with separation of:

* Models
* Database
* CRUD operations
* API routes

---

## Folder Structure

```text
TODO-USING-SQLALCHEMY/
│
├── .venv/                  # Virtual environment
│
├── alembic/               # Migration system
│   ├── __pycache__/
│   ├── versions/          # Migration files
│   ├── env.py             # Migration config
│   ├── script.py.mako     # Migration template
│   ├── README             # Alembic notes
│
├── app/                   # Main application
│   ├── __pycache__/
│
│   ├── crud/              # Database operations layer
│   │   ├── todo_crud.py
│   │   ├── user_crud.py
│
│   ├── db/                # Database configuration
│   │   ├── base.py        # Base model
│   │   ├── session.py     # DB connection
│
│   ├── models/            # ORM models
│   │   ├── todo.py
│   │   ├── user.py
│
│   ├── main.py            # FastAPI application
│
├── .gitignore
├── alembic.ini            # Alembic config
├── pyproject.toml
├── requirements.txt
├── README.md
├── test.db                # SQLite DB
├── todo.db                # SQLite DB
└── uv.lock
```

---

## Architecture Overview

```text
Client → FastAPI → CRUD → SQLAlchemy ORM → Database
```

---

## Database Design

### Users Table

| Column | Type    | Description  |
| ------ | ------- | ------------ |
| id     | Integer | Primary Key  |
| name   | String  | User name    |
| email  | String  | Unique email |

---

### Todos Table

| Column      | Type    | Description |
| ----------- | ------- | ----------- |
| id          | Integer | Primary Key |
| title       | String  | Task title  |
| description | String  | Details     |
| completed   | Boolean | Status      |
| user_id     | Integer | Foreign Key |

---

### Relationship

```text
One User → Many Todos
```

---

## Core Concepts Explained

### 1. FastAPI

* High-performance Python framework
* Auto API docs → `/docs`
* Dependency Injection system

---

### 2. SQLAlchemy ORM

* Converts Python classes → database tables
* Handles queries without raw SQL

---

### 3. Session

* Controls DB transactions
* Used for:

  * add()
  * commit()
  * query()

---

### 4. CRUD Layer

* Separates business logic
* Improves maintainability

---

### 5. Relationships

```python
relationship("Todo", back_populates="owner")
```

---

### 6. Alembic

* Database version control
* Tracks schema changes

---

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv .venv
```

---

### 2. Activate Environment

```bash
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Configuration

```python
DATABASE_URL = "sqlite:///./test.db"
```

---

## Alembic Commands

### Initialize

```bash
alembic init alembic
```

---

### Create Migration

```bash
alembic revision -m "initial"
```

---

### Auto Generate Migration

```bash
alembic revision --autogenerate -m "create tables"
```

---

### Apply Migration

```bash
alembic upgrade head
```

---

### Rollback Migration

```bash
alembic downgrade -1
```

---

## Run Application

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

* Swagger UI → http://127.0.0.1:8000/docs
* ReDoc → http://127.0.0.1:8000/redoc

---

## API Endpoints

### Users

| Method | Endpoint    | Description |
| ------ | ----------- | ----------- |
| POST   | /users/     | Create user |
| GET    | /users/     | Get users   |
| GET    | /users/{id} | Get user    |

---

### Todos

| Method | Endpoint    | Description |
| ------ | ----------- | ----------- |
| POST   | /todos/     | Create todo |
| GET    | /todos/     | Get todos   |
| GET    | /todos/{id} | Get todo    |

---

### JOIN

| Method | Endpoint           | Description       |
| ------ | ------------------ | ----------------- |
| GET    | /todos-with-users/ | Todos + User data |

---

## Features

✔️ CRUD operations
✔️ Filtering
✔️ Pagination
✔️ Sorting
✔️ JOIN queries
✔️ Relationship handling
✔️ Migration system

---

## Git Workflow

### Add files

```bash
git add .
```

---

### Commit

```bash
git commit -m "Your message"
```

---

### Push

```bash
git push origin main
```

---

### Warning

```text
LF will be replaced by CRLF
```
* Not an error 

---

## Example Response

```json
{
  "todo_id": 1,
  "title": "Learn FastAPI",
  "completed": false,
  "user": {
    "id": 1,
    "name": "Ashish",
    "email": "ashish@example.com"
  }
}
```



