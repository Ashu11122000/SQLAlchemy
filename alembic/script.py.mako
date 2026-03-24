# """ ... """ = This is a multi-line string (docstring)
# Alembic uses this as the header of the migration file

"""
# ${message} = placeholder variable
# → When you run: alembic revision -m "create user table"
# → ${message} becomes: "create user table"
# → This line describes what this migration does
${message}

# Revision ID: unique identifier of this migration
# ${up_revision} = auto-generated unique ID (like 'a1b2c3d4')
# This ID helps Alembic track migration order
Revision ID: ${up_revision}

# Revises: previous migration ID
# ${down_revision | comma,n}
# → down_revision = parent migration
# → comma,n = formatting filter (handles multiple parents if branching exists)
Revises: ${down_revision | comma,n}

# Create Date: timestamp when migration was created
# ${create_date} = auto-filled date and time
Create Date: ${create_date}
"""


# Importing typing utilities
# typing = built-in module for type hints
from typing import Sequence, Union
# Sequence = represents ordered collection (like list, tuple)
# Union = allows multiple possible types (e.g., str OR list)


# Importing Alembic operations module
# op = object used to perform DB operations (create table, add column, etc.)
from alembic import op


# Importing SQLAlchemy as alias "sa"
# sa = commonly used shorthand for SQLAlchemy
# Used for defining columns, types (Integer, String, etc.)
import sqlalchemy as sa


# ${imports if imports else ""}
# → Template placeholder
# → If Alembic needs extra imports (like UUID, JSON, etc.), they appear here
# → Otherwise, this line becomes empty
${imports if imports else ""}


# revision identifiers, used by Alembic.

# revision: current migration ID
# str = type hint (means this variable is a string)
# ${repr(up_revision)} = actual value inserted (e.g., 'a1b2c3d4')
revision: str = ${repr(up_revision)}


# down_revision: previous migration ID
# Union[str, Sequence[str], None] means:
# → can be:
#    - str (single parent migration)
#    - list/tuple (multiple parents in branching)
#    - None (first migration)
# ${repr(down_revision)} = actual value inserted
down_revision: Union[str, Sequence[str], None] = ${repr(down_revision)}


# branch_labels:
# Used when working with multiple branches in migrations
# Usually None unless you explicitly use branching
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}


# depends_on:
# Used when this migration depends on another migration (rare use case)
# Helps control execution order in complex scenarios
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


# Function to apply migration (UPGRADE database)
def upgrade() -> None:
    """Upgrade schema."""
    
    # ${upgrades if upgrades else "pass"}
    # Template placeholder:
    # → If autogenerate detects changes → code is inserted here
    # Example:
    # op.create_table(...)
    # op.add_column(...)
    #
    # If no changes detected → "pass" is inserted
    ${upgrades if upgrades else "pass"}


# Function to revert migration (DOWNGRADE database)
def downgrade() -> None:
    """Downgrade schema."""
    
    # ${downgrades if downgrades else "pass"}
    # Template placeholder:
    # → Reverse of upgrade()
    # Example:
    # op.drop_table(...)
    # op.drop_column(...)
    #
    # If no downgrade logic → "pass"
    ${downgrades if downgrades else "pass"}