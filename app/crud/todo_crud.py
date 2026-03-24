# Importing Session class from sqlalchemy.orm
# sqlalchemy = ORM library
# orm = Object Relational Mapper module
# Session = represents a database session (connection + transaction handler)
# Used to interact with DB (add, update, delete, query)
from sqlalchemy.orm import Session


# Importing select function from sqlalchemy
# select() = used to create SQL SELECT queries in Python
# It replaces raw SQL like: SELECT * FROM table
from sqlalchemy import select


# Importing Todo model from your project
# Todo = ORM model class representing "todo" table in DB
from app.models.todo import Todo


# Importing User model
# User = ORM model class representing "user" table
from app.models.user import User


# Create Todo

# def = keyword to define a function
# create_todo = function name (used to create a new todo record)
def create_todo(
    
    # db: Session
    # db = variable name (database session object)
    # Session = type hint (tells this parameter must be a Session object)
    db: Session,
    
    # title: str
    # title = parameter name
    # str = string type (text data)
    title: str,
    
    # description: str
    # description = parameter
    # str = text
    description: str,
    
    # user_id: int
    # user_id = foreign key referencing User table
    # int = integer type
    user_id: int
):
    
    # Creating a new Todo object (row)
    # Todo(...) = calling model constructor
    todo = Todo(
        
        # title=title
        # left side = column name in DB
        # right side = function parameter value
        title=title,
        
        # description column assignment
        description=description,
        
        # foreign key assignment
        user_id=user_id
    )
    
    # db.add(todo)
    # add() = tells SQLAlchemy to insert this object into DB
    db.add(todo)
    
    # db.commit()
    # commit() = saves transaction permanently to database
    db.commit()
    
    # db.refresh(todo)
    # refresh() = reloads object from DB
    # useful to get auto-generated values (like id)
    db.refresh(todo)
    
    # return = send result back to caller
    return todo


# Get Todo by ID

# Function to fetch a single todo using its ID
def get_todo_by_id(db: Session, todo_id: int):
    
    # stmt = SQL statement (query)
    stmt = select(Todo).where(
        
        # Todo.id == todo_id
        # Todo.id = column
        # == = comparison operator
        # todo_id = input value
        Todo.id == todo_id
    )
    
    # Execute query
    result = db.execute(stmt)
    
    # scalar_one_or_none():
    # → returns single result OR None
    # → if no row found → returns None
    # → if multiple rows → raises error
    return result.scalar_one_or_none()


# Get All Todos (Filtering + Ordering + Pagination)

def get_all_todos(
    db: Session,
    
    # skip = number of rows to skip
    # default = 0
    skip: int = 0,
    
    # limit = max number of rows to return
    # default = 10
    limit: int = 10,
    
    # completed = filter by completed status
    # bool | None = can be True, False, or None
    # None means no filtering
    completed: bool | None = None,
    
    # user_id filter
    user_id: int | None = None,
    
    # order_by = column name to sort results
    order_by: str = "id"
):
    
    # Base query
    stmt = select(Todo)

    # 🔹 Filtering
    
    # If completed is provided (True/False)
    if completed is not None:
        
        # Add WHERE condition
        stmt = stmt.where(
            Todo.completed == completed
        )

    # If user_id filter provided
    if user_id is not None:
        
        # Add WHERE condition
        stmt = stmt.where(
            Todo.user_id == user_id
        )

    # Ordering
    
    # Sort by title
    if order_by == "title":
        stmt = stmt.order_by(Todo.title)
    
    # Sort by completed status
    elif order_by == "completed":
        stmt = stmt.order_by(Todo.completed)
    
    # Default sorting by id
    else:
        stmt = stmt.order_by(Todo.id)

    # Pagination
    
    # offset(skip) = skip first N rows
    # limit(limit) = limit number of rows
    stmt = stmt.offset(skip).limit(limit)

    # Execute query
    result = db.execute(stmt)
    
    # scalars() = extracts only model objects (not tuples)
    # all() = returns all results as list
    return result.scalars().all()


# JOIN Query (Todo + User)
def get_todos_with_users(db: Session):
    
    # stmt = SQL query
    stmt = (
        
        # select both Todo and User tables
        select(Todo, User)
        
        # join = SQL JOIN
        # User = table to join
        # condition = Todo.user_id == User.id
        .join(User, Todo.user_id == User.id)
    )

    # Execute query
    result = db.execute(stmt)

    # result.all()
    # returns list of tuples
    # each tuple = (Todo object, User object)
    return result.all()


# Get Todos of a Specific User (using JOIN)

def get_todos_by_user(db: Session, user_id: int):
    
    # Build query
    stmt = (
        
        # select only Todo
        select(Todo)
        
        # join User table automatically using relationship
        .join(User)
        
        # filter where User.id matches
        .where(User.id == user_id)
    )

    # Execute query
    result = db.execute(stmt)
    
    # scalars() = extract only Todo objects
    # all() = return list
    return result.scalars().all()