# Importing column data types from sqlalchemy

# String = used for text data (VARCHAR in SQL)
# Integer = used for numeric values (INT in SQL)
from sqlalchemy import String, Integer


# Importing ORM utilities from sqlalchemy.orm

# Mapped = used for type annotations (SQLAlchemy 2.0 style)
# → tells ORM that attribute is mapped to a DB column

# mapped_column = used to define table columns
# → replaces old Column() syntax

# relationship = defines relationship between tables (ORM-level linking)
from sqlalchemy.orm import Mapped, mapped_column, relationship


# Importing Base class (parent class for all models)
# Base = provides metadata and ORM functionality
from app.db.base import Base


# class = keyword to define class
# User = class name (represents "users" table)
# (Base) = inheritance → tells SQLAlchemy this is a table model
class User(Base):
    
    # __tablename__ = special variable
    # → defines actual table name in database
    __tablename__ = "users"

    # -------------------------------
    # Primary Key
    # -------------------------------

    # id = column name
    # Mapped[int] = mapped to integer column
    
    id: Mapped[int] = mapped_column(
        
        # Integer = SQL data type
        Integer,
        
        # primary_key=True
        # → uniquely identifies each row
        primary_key=True,
        
        # index=True
        # → creates index for faster queries
        index=True
    )

    # -------------------------------
    # Columns
    # -------------------------------

    # name column
    
    name: Mapped[str] = mapped_column(
        
        # String(100) = VARCHAR(100)
        # max 100 characters
        String(100),
        
        # nullable=False
        # → required field (cannot be NULL)
        nullable=False
    )


    # email column
    
    email: Mapped[str] = mapped_column(
        
        # String(100) = VARCHAR(100)
        String(100),
        
        # unique=True
        # → ensures no duplicate emails
        # → creates UNIQUE constraint in DB
        
        unique=True,
        
        # nullable=False
        # → must have value
        nullable=False
    )

    # -------------------------------
    # Relationship with Todo
    # -------------------------------

    # todos = attribute name (Python side)
    # represents list of Todo objects related to this user
    
    todos = relationship(
        
        # "Todo" = related model name (string to avoid circular import)
        "Todo",
        
        # back_populates="owner"
        # → connects with Todo.owner
        # → creates bidirectional relationship
        
        back_populates="owner",
        
        # cascade="all, delete"
        # → defines behavior when user is deleted
        # "all" = apply all operations (save, update, delete)
        # "delete" = delete related todos when user is deleted
        
        cascade="all, delete"
    )