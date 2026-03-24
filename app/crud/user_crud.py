# Importing Session class from sqlalchemy.orm
# sqlalchemy = Python SQL toolkit and ORM library
# orm = Object Relational Mapping module (maps Python classes to DB tables)
# Session = class used to manage database connection and transactions
# It allows us to perform operations like add(), commit(), query(), etc.
from sqlalchemy.orm import Session


# Importing select function from sqlalchemy
# select() = used to create SQL SELECT queries in Python
# Equivalent to writing raw SQL like: SELECT * FROM user
from sqlalchemy import select


# Importing User model from your project
# User = ORM class that represents "users" table in database
# It contains columns like id, name, email
from app.models.user import User


# ✅ Create User

# def = keyword used to define a function
# create_user = function name (used to create a new user)
def create_user(
    
    # db: Session
    # db = variable holding database session object
    # Session = type hint (ensures db is a Session object)
    db: Session,
    
    # name: str
    # name = user name input
    # str = string data type (text)
    name: str,
    
    # email: str
    # email = user email input
    # str = string type
    email: str
):
    
    # Creating a new User object (represents a row in DB)
    # User(...) = calling constructor of User model
    user = User(
        
        # Assigning name column value
        # left = DB column, right = function parameter
        name=name,
        
        # Assigning email column value
        email=email
    )
    
    # db.add(user)
    # add() = adds object to session (prepares INSERT query)
    db.add(user)
    
    # db.commit()
    # commit() = saves transaction permanently to database
    db.commit()
    
    # db.refresh(user)
    # refresh() = reloads object from database
    # useful to get auto-generated fields (like id)
    db.refresh(user)
    
    # return = send created user back to caller
    return user


# ✅ Get User by ID

# Function to fetch user using primary key (id)
def get_user_by_id(
    
    # db session object
    db: Session,
    
    # user_id = ID of user
    # int = integer type
    user_id: int
):
    
    # stmt = SQL statement (query object)
    stmt = select(User).where(
        
        # User.id = column
        # == = comparison operator
        # user_id = input value
        User.id == user_id
    )
    
    # Execute query using session
    result = db.execute(stmt)
    
    # scalar_one_or_none()
    # → returns exactly one result OR None
    # → if no record found → returns None
    # → if multiple found → raises error
    return result.scalar_one_or_none()


# ✅ Get User by Email

# Function to fetch user using email
def get_user_by_email(
    
    db: Session,
    
    # email parameter
    # str = text
    email: str
):
    
    # Build SELECT query
    stmt = select(User).where(
        
        # Compare email column with input
        User.email == email
    )
    
    # Execute query
    result = db.execute(stmt)
    
    # Return single result or None
    return result.scalar_one_or_none()


# ✅ Get All Users (with filtering & ordering)

# Function to get list of users with pagination and sorting
def get_all_users(
    
    db: Session,
    
    # skip = number of records to skip
    # default = 0 (start from beginning)
    skip: int = 0,
    
    # limit = maximum number of records to return
    # default = 10
    limit: int = 10,
    
    # order_by = column name for sorting
    # default = "id"
    order_by: str = "id"
):
    
    # Base query (SELECT * FROM user)
    stmt = select(User)

    # 🔹 Ordering (sorting results)
    
    # If order_by = "name"
    if order_by == "name":
        
        # ORDER BY name column
        stmt = stmt.order_by(User.name)
    
    # If order_by = "email"
    elif order_by == "email":
        
        # ORDER BY email column
        stmt = stmt.order_by(User.email)
    
    # Default case (order by id)
    else:
        stmt = stmt.order_by(User.id)

    # 🔹 Pagination
    
    # offset(skip) = skip first N records
    # limit(limit) = return only N records
    stmt = stmt.offset(skip).limit(limit)

    # Execute query
    result = db.execute(stmt)
    
    # scalars() = extracts only User objects (not tuples)
    # all() = returns list of all results
    return result.scalars().all()