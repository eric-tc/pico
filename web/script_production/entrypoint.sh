#!/bin/sh

# Wait for the PostgreSQL service to be available
echo "Waiting for postgres..."
while ! nc -z postgres 5432; do
  sleep 1
done
echo "Postgres is up!"

flask db init

flask db migrate -m "initial migration"

# Run Flask database migrations
flask db upgrade


