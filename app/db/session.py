# Importing create_engine function from sqlalchemy
# sqlalchemy = Python ORM & SQL toolkit
# create_engine = function used to create a database engine (core connection interface)
# Engine = responsible for managing DB connections and executing SQL
from sqlalchemy import create_engine


# Importing sessionmaker and Session from sqlalchemy.orm
# sessionmaker = factory function to create new Session objects
# Session = class representing a database session (connection + transaction)
from sqlalchemy.orm import sessionmaker, Session


# Database URL

# DATABASE_URL = variable storing connection string
# "sqlite:///./test.db" breakdown:
# sqlite = database type (SQLite)
# /// = relative file path indicator
# ./test.db = database file in current directory
DATABASE_URL = "sqlite:///./test.db"


# Engine with connection pooling

# engine = variable storing Engine object
# create_engine(...) = creates connection to database
engine = create_engine(
    
    # DATABASE_URL = connection string
    DATABASE_URL,
    
    # connect_args = extra arguments for DB connection
    # {"check_same_thread": False}:
    # → SQLite restriction: same thread must use connection
    # → False allows multiple threads (needed for FastAPI)
    connect_args={"check_same_thread": False},  # Required for SQLite
    
    # pool_size = number of permanent connections kept open
    # Example: 5 connections always ready
    pool_size=5,
    
    # max_overflow = extra temporary connections allowed
    # Example: can go up to 5 + 10 = 15 connections
    max_overflow=10,
    
    # pool_timeout = seconds to wait before raising error if no connection available
    pool_timeout=30,
    
    # pool_recycle = time (seconds) after which connection is refreshed
    # helps prevent stale connections
    pool_recycle=1800,
)


# Session factory

# SessionLocal = factory to create new Session objects
# sessionmaker(...) returns a class that generates sessions
SessionLocal = sessionmaker(
    
    # autocommit=False
    # → changes are NOT automatically saved
    # → must call db.commit() manually
    autocommit=False,
    
    # autoflush=False
    # → prevents automatic sending of changes to DB
    # → gives manual control
    autoflush=False,
    
    # bind=engine
    # → connects session to database engine
    bind=engine
)


# Dependency for FastAPI (with typing)

# def = define function
# get_db = function name (used as dependency in FastAPI)
def get_db() -> Session:
    
    # -> Session = return type hint
    # indicates function will yield a Session object
    
    # db = session instance created from SessionLocal
    db = SessionLocal()
    
    try:
        # yield = keyword used in generators
        # returns db to FastAPI endpoint
        # keeps function alive until request is complete
        yield db
    
    finally:
        # finally block always executes (even if error occurs)
        
        # db.close() = closes DB connection
        # releases connection back to pool
        db.close()