# Task Overview

You are joining Utkrusht’s inventory management product team. The company operates an internal tool for warehouse teams to track available items in real time. The FastAPI application already contains route handlers for adding and viewing products, but does not yet have the database schema or data logic implemented. You are responsible for designing the product inventory schema in PostgreSQL, implementing async database operations to read and write product records, and ensuring good data integrity and performance best practices. This will directly impact how accurately and efficiently warehouse staff can check and update stock levels.

# Guidance

- Route handlers are already implemented in `app/main.py`.
- Place your database models in `app/models.py` and your async CRUD operations in `app/database.py`.
- Define your PostgreSQL schema in `schema.sql` and use indexes as needed.
- Use the `run.sh` script to initialize Docker containers, set up the schema, and install dependencies for the environment.

# Objectives

- Create a normalized PostgreSQL table called `products` with appropriate columns (id, name, description, quantity, price), data types, and constraints (pk, unique, not null, etc.).
- Implement all async-compatible CRUD logic for adding and retrieving product records using SQLAlchemy and asyncpg within the FastAPI codebase.
- Ensure new products can be added and a listing of all products can be fetched using efficient, indexed queries.
- Integrate the models and database layer with the provided FastAPI endpoints—no changes to API signatures allowed.

# How to Verify

- Add a product using the `/products` POST endpoint and verify it appears in the `/products` GET listing.
- Confirm that products persist in the PostgreSQL database across container restarts.
- Check that constraints prevent duplicate names or missing required fields.
- Use psql or pgAdmin/DBeaver to verify the schema and index usage (try `EXPLAIN` on product queries).
- Confirm all DB operations are non-blocking (the API stays responsive on concurrent calls).
