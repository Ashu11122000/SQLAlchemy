# 🧱 Alembic Migration Guide

## Overview
Alembic is a lightweight database migration tool for Python that works with 

# SQLAlchemy
It allows you to:
* Track database schema changes
* Apply incremental updates (migrations)
* Roll back changes safely
* Maintain version control for your database

-> Think of Alembic as Git for your database schema

---

## Why Alembic is Needed
Without Alembic:
* You manually update database tables
* No version control
* Hard to track changes 

With Alembic:
* Schema changes are tracked 
* Easy upgrades & downgrades 
* Works with teams 

---

## Core Concepts

### 1. Migration
A migration is a Python script that describes changes in your database schema.
Example:

```bash
op.create_table("users", ...)
```

---

### 2. Revision ID
Each migration has a unique ID:
```bash
revision = "a1b2c3d4"
```
* Used to track migration order

---

### 3. Migration Chain

```bash
None → a1 → b2 → c3
```
* `down_revision` connects migrations
* Works like a linked list

---

### 4. upgrade() vs downgrade()

| Function    | Purpose          |
| ----------- | ---------------- |
| upgrade()   | Apply changes    |
| downgrade() | Rollback changes |

---

### 5. env.py
* Core configuration file
Responsibilities:

* Connect to database
* Load models
* Run migrations

---

### 6. script.py.mako
Template used to generate migration files
* Defines structure of migration
* Uses placeholders like `${up_revision}`

---

### 7. target_metadata

```bash
target_metadata = Base.metadata
```
* Provides table info to Alembic
* Used for auto-detection

---

### 8. Autogenerate Feature
Command:
```bash
alembic revision --autogenerate -m "message"
```

Automatically detects:
* New tables
* Column changes
* Constraints

---

## Alembic Project Structure

```text
alembic/
│
├── env.py              # Migration environment config
├── script.py.mako      # Migration template
├── versions/           # All migration files
│
├── alembic.ini         # Configuration file
```

---

## Setup & Installation

### 1. Install Alembic

```bash
pip install alembic
```

---

### 2. Initialize Alembic

```bash
alembic init alembic
```

---

### 3. Configure Database (alembic.ini)

```ini
sqlalchemy.url = postgresql://user:password@localhost/db_name
```

---

### 4. Link Models (env.py)

```python
from app.db.base import Base
target_metadata = Base.metadata
```

---

## 🔄 Migration Commands

### Create Migration

```bash
alembic revision -m "create user table"
```

---

### Auto Generate Migration

```bash
alembic revision --autogenerate -m "add new column"
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

### Show History

```bash
alembic history
```

---

## Common Operations (Using `op`)

```python
op.create_table()
op.drop_table()
op.add_column()
op.drop_column()
```

---

## Use Cases

* Backend APIs (FastAPI, Django, Flask)
* Production database management
* Schema version control
* Team collaboration
* Continuous deployment pipelines

---

## Common Errors & Fixes

### Tables not detected
Fix:

```python
from app.models import user, todo
```

---

### Empty migration
Cause:
* Models not imported
* metadata not linked
---

### Type changes not detected
 Fix:

```python
compare_type=True
```

---

## Your Git Workflow (Based on Your Commands)

### Add File

```bash
git add alembic/env.py
```

---

### Commit Changes

```bash
git commit -m "Adding updated alembic env.py configuration file"
```

---

### Push to GitHub

```bash
git push origin main
```

---

### Add Template File

```bash
git add alembic/script.py.mako
```

---

### Commit Template

```bash
git commit -m "Added Alembic script.py.mako template"
```

---

### Push Again

```bash
git push origin main
```

---

## Git Warning (LF vs CRLF)

```text
LF will be replaced by CRLF
```

Meaning:
* LF = Linux line endings
* CRLF = Windows line endings

* Not an error 
* Just a warning

Fix (optional):

```bash
git config --global core.autocrlf true
```

---
