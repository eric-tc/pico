#!/bin/sh

# Wait for the PostgreSQL service to be available
echo "Waiting for postgres..."
while ! nc -z postgres_prod 5432; do
  sleep 1
done
echo "Postgres is up!"

if [ ! -f /data/initialized ]; then
  echo "Running database initialization..."
  flask db init
  # Run Flask database migrations
  flask db upgrade
  # Create a file to mark initialization as done
  touch /app/initialized
else
  echo "Database already initialized"
  flask db upgrade
fi
exec "$@"