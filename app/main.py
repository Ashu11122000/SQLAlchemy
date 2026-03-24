# Importing FastAPI and utilities

# FastAPI = main class to create API application
# Depends = used for dependency injection (e.g., database session)
# HTTPException = used to raise HTTP errors (like 404, 400)
from fastapi import FastAPI, Depends, HTTPException


# Importing Session from SQLAlchemy ORM
# Session = database session for executing queries
from sqlalchemy.orm import Session


# Importing database utilities

# get_db = function that provides DB session (dependency)
# engine = database engine (connection to DB)
from app.db.session import get_db, engine


# Importing Base class (contains metadata of all models)
# Base.metadata = contains all table definitions
from app.db.base import Base


# Importing CRUD modules

# user_crud = file containing user database operations
# todo_crud = file containing todo database operations
from app.crud import user_crud, todo_crud


# ✅ Create tables (for development only)

# Base.metadata.create_all()
# → creates all tables in database if not exist
# bind=engine → tells SQLAlchemy which DB to use
# ⚠️ Only for development (not recommended in production)
Base.metadata.create_all(bind=engine)


# Creating FastAPI application instance
app = FastAPI()


# ------------------- USER APIs -------------------

# Duplicate import (not needed, but harmless)
from fastapi import FastAPI

# Duplicate app creation (overwrites previous app)
app = FastAPI()


# Root endpoint (GET request)

# @app.get("/") = decorator
# → defines API endpoint for GET method at "/"
@app.get("/")
def read_root():
    
    # return = sends JSON response
    return {"message": "API is working 🚀"}


# Create User API (POST)

# @app.post("/users/") = POST endpoint
@app.post("/users/")
def create_user(
    
    # name = query parameter (string)
    name: str,
    
    # email = query parameter (string)
    email: str,
    
    # db = database session dependency
    # Depends(get_db) = injects DB session automatically
    db: Session = Depends(get_db)
):
    
    # Check if user already exists
    existing_user = user_crud.get_user_by_email(db, email)
    
    if existing_user:
        
        # Raise HTTP error (400 Bad Request)
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # Create new user
    return user_crud.create_user(db, name, email)


# Get All Users API (GET)

@app.get("/users/")
def get_users(
    
    # skip = pagination offset
    skip: int = 0,
    
    # limit = number of records
    limit: int = 10,
    
    # order_by = sorting column
    order_by: str = "id",
    
    # DB dependency
    db: Session = Depends(get_db)
):
    
    # Call CRUD function
    return user_crud.get_all_users(db, skip, limit, order_by)


# Get User by ID API

@app.get("/users/{user_id}")
def get_user(
    
    # user_id = path parameter (comes from URL)
    user_id: int,
    
    db: Session = Depends(get_db)
):
    
    # Fetch user
    user = user_crud.get_user_by_id(db, user_id)
    
    if not user:
        
        # If not found → raise 404 error
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    return user


# ------------------- TODO APIs -------------------

# Create Todo API

@app.post("/todos/")
def create_todo(
    
    title: str,
    description: str,
    user_id: int,
    
    db: Session = Depends(get_db)
):
    
    # Check if user exists
    user = user_crud.get_user_by_id(db, user_id)
    
    if not user:
        
        # If user not found → error
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Create todo
    return todo_crud.create_todo(db, title, description, user_id)


# Get All Todos API

@app.get("/todos/")
def get_todos(
    
    # Pagination
    skip: int = 0,
    limit: int = 10,
    
    # Filtering
    completed: bool | None = None,
    user_id: int | None = None,
    
    # Sorting
    order_by: str = "id",
    
    db: Session = Depends(get_db)
):
    
    # Call CRUD with filters, sorting, pagination
    return todo_crud.get_all_todos(
        db,
        skip,
        limit,
        completed,
        user_id,
        order_by
    )


# Get Todo by ID API

@app.get("/todos/{todo_id}")
def get_todo(
    
    todo_id: int,
    
    db: Session = Depends(get_db)
):
    
    # Fetch todo
    todo = todo_crud.get_todo_by_id(db, todo_id)
    
    if not todo:
        
        # Raise 404 if not found
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )
    
    return todo


# ------------------- JOIN APIs -------------------

# Get Todos with User details

@app.get("/todos-with-users/")
def get_todos_with_users(
    
    db: Session = Depends(get_db)
):
    
    # Fetch joined data (Todo + User)
    data = todo_crud.get_todos_with_users(db)

    # Format response manually
    result = []
    
    # Loop through each tuple (todo, user)
    for todo, user in data:
        
        result.append({
            
            # Todo fields
            "todo_id": todo.id,
            "title": todo.title,
            "completed": todo.completed,
            
            # Nested user object
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
        })

    return result