#!/bin/bash
set -e

echo "Starting Docker containers..."
docker-compose up -d --build

echo "Waiting for PostgreSQL to be ready..."
docker-compose exec -T db bash -c 'until pg_isready -U inv_user; do sleep 1; done;'

echo "Applying initial database schema..."
docker cp schema.sql $(docker-compose ps -q db):/schema.sql
docker-compose exec -T db bash -c 'psql -U inv_user -d inventory_db -f /schema.sql'

echo "Setup complete. FastAPI running at http://localhost:8000"
