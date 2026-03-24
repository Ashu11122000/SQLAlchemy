# Importing DeclarativeBase class from sqlalchemy.orm
# sqlalchemy = Python ORM library used for database interaction
# orm = Object Relational Mapping module
# DeclarativeBase = base class provided by SQLAlchemy (new style in SQLAlchemy 2.0)
# It is used to create a base class for all models (tables)
from sqlalchemy.orm import DeclarativeBase


# Base class for all models

# class = keyword used to define a class in Python
# Base = name of the class (commonly used name in SQLAlchemy projects)
# (DeclarativeBase) = inheritance
# → Base class is inheriting from DeclarativeBase
# → This means Base will get all ORM capabilities (table mapping, metadata, etc.)
class Base(DeclarativeBase):
    
    # pass = keyword used when no additional code is needed
    # It means: "This class doesn't add anything extra right now"
    # Base still works because it inherits functionality from DeclarativeBase
    pass