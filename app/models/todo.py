# Importing column types and constraints from sqlalchemy

# String = data type for text (VARCHAR in SQL)
# Integer = data type for numbers (INT in SQL)
# Boolean = data type for True/False values
# ForeignKey = used to create relationship between tables (link columns)
from sqlalchemy import String, Integer, Boolean, ForeignKey


# Importing ORM utilities

# Mapped = type annotation used in SQLAlchemy 2.0
# → tells ORM that this attribute is mapped to a DB column

# mapped_column = function used to define a column
# → replaces old Column() syntax

# relationship = used to define relationship between tables (ORM-level linking)
from sqlalchemy.orm import Mapped, mapped_column, relationship


# Importing Base class (parent for all models)
# Base = contains metadata and ORM configuration
from app.db.base import Base


# class = keyword to define class
# Todo = class name (represents "todos" table in DB)
# (Base) = inheritance → tells SQLAlchemy this is a table model
class Todo(Base):
    
    # __tablename__ = special variable
    # → defines table name in database
    # → "todos" = actual table name
    __tablename__ = "todos"

    # -------------------------------
    # Primary Key
    # -------------------------------

    # id = column name in model
    # Mapped[int] = type annotation (mapped to integer column)
    # mapped_column(...) = defines column properties
    
    id: Mapped[int] = mapped_column(
        
        # Integer = SQL data type
        Integer,
        
        # primary_key=True
        # → marks this column as primary key
        # → uniquely identifies each row
        primary_key=True,
        
        # index=True
        # → creates index for faster searching
        index=True
    )

    # -------------------------------
    # Columns
    # -------------------------------

    # title column
    
    # Mapped[str] = mapped string column
    title: Mapped[str] = mapped_column(
        
        # String(200) = VARCHAR(200)
        # max length = 200 characters
        String(200),
        
        # nullable=False
        # → column cannot be NULL (must have value)
        nullable=False
    )


    # description column
    
    description: Mapped[str] = mapped_column(
        
        # String(500) = max 500 characters
        String(500),
        
        # nullable=True
        # → optional field (can be NULL)
        nullable=True
    )


    # completed column
    
    completed: Mapped[bool] = mapped_column(
        
        # Boolean type (True/False)
        Boolean,
        
        # default=False
        # → default value when not provided
        default=False
    )

    # -------------------------------
    # Foreign Key
    # -------------------------------

    # user_id column
    
    user_id: Mapped[int] = mapped_column(
        
        # ForeignKey("users.id")
        # → links this column to users table
        # → "users.id" means:
        #     table = users
        #     column = id
        ForeignKey("users.id")
    )

    # -------------------------------
    # Relationship with User
    # -------------------------------

    # owner = attribute name (Python-side relation)
    
    owner = relationship(
        
        # "User" = related model name (string reference)
        # string used to avoid circular import
        
        "User",
        
        # back_populates="todos"
        # → connects with User model
        # → User model must have: todos = relationship(...)
        # → creates bidirectional relationship
        
        back_populates="todos"
    )