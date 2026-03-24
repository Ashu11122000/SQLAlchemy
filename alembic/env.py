# Importing the function `fileConfig` from the module `logging.config`
# logging = Python's built-in module used for logging (printing logs like INFO, ERROR, etc.)
# config = submodule of logging that helps configure logging settings
# fileConfig = function that reads logging configuration from a file (like alembic.ini)
from logging.config import fileConfig


# Importing `engine_from_config` from SQLAlchemy
# engine = core interface to the database (manages DB connections)
# from_config = means it creates engine using configuration (like alembic.ini)
from sqlalchemy import engine_from_config


# Importing `pool` module from SQLAlchemy
# pool = manages database connections (reuse, open, close connections efficiently)
from sqlalchemy import pool


# Importing `context` from Alembic
# context = main Alembic object that controls migration execution
# It provides functions like configure(), run_migrations(), etc.
from alembic import context


# ✅ Import your Base and models

# Importing Base class from your project
# Base = parent class for all SQLAlchemy models (created using declarative_base())
# It contains metadata (info about tables, columns, relationships)
from app.db.base import Base


# Importing models (VERY IMPORTANT)
# user, todo = your model files
# Why import?
# → So Alembic can detect tables inside these models
# → If not imported, Alembic will think tables don’t exist
from app.models import user, todo  # VERY IMPORTANT (register models)


# this is the Alembic Config object
# context.config = gives access to alembic.ini configuration
# config = object storing settings like DB URL, logging config, etc.
config = context.config


# Setup logging
# config.config_file_name = path of config file (like alembic.ini)
# If it exists (not None), then configure logging
if config.config_file_name is not None:
    # fileConfig() reads logging configuration from file
    # and applies logging settings (format, level, handlers)
    fileConfig(config.config_file_name)


# ✅ Link metadata

# Base.metadata = contains all table definitions from your models
# Alembic uses this metadata to compare with database schema
# and generate migrations
target_metadata = Base.metadata


# Function to run migrations in OFFLINE mode
# offline = no actual DB connection required
# migrations are generated as SQL scripts only
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""

    # Get database URL from alembic config file
    # "sqlalchemy.url" = key in alembic.ini
    url = config.get_main_option("sqlalchemy.url")
    
    # Configure Alembic context
    context.configure(
        url=url,                         # Database URL (no connection, just string)
        target_metadata=target_metadata, # Metadata for auto-detection
        literal_binds=True,              # Convert values into raw SQL (no placeholders)
        compare_type=True,               # ✅ Detect column type changes (VERY IMPORTANT)
    )

    # Begin a transaction block
    # even in offline mode, Alembic simulates transaction
    with context.begin_transaction():
        
        # Run migrations (generate SQL)
        context.run_migrations()


# Function to run migrations in ONLINE mode
# online = actual connection to database
def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    
    # Create database engine using config
    connectable = engine_from_config(
        
        # config.get_section(...) gets DB settings from alembic.ini
        # config.config_ini_section usually = "alembic"
        config.get_section(config.config_ini_section),
        
        # prefix="sqlalchemy." means:
        # only use config keys starting with "sqlalchemy."
        prefix="sqlalchemy.",
        
        # poolclass = defines connection pooling behavior
        # NullPool = no connection reuse (good for migrations)
        poolclass=pool.NullPool,
    )

    # Establish actual connection to database
    with connectable.connect() as connection:
        
        # Configure Alembic context with live connection
        context.configure(
            connection=connection,        # Active DB connection
            target_metadata=target_metadata, # Metadata for comparison
            compare_type=True,            # ✅ Detect column changes
        )

        # Begin transaction
        with context.begin_transaction():
            
            # Execute migrations (apply changes to DB)
            context.run_migrations()


# Check if Alembic is running in offline mode
# context.is_offline_mode() returns True/False
if context.is_offline_mode():
    
    # If offline → generate SQL scripts only
    run_migrations_offline()
else:
    
    # If online → connect to DB and apply migrations
    run_migrations_online()