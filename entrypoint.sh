#!/bin/bash

echo "Waiting for postgres..."
sleep 5
echo "PostgreSQL started"

echo "Migrating database..."
python manage.py migrate --noinput
echo "Database migrated"

echo "Collecting static files..."
python manage.py collectstatic --noinput
echo "Static files collected"

echo "Starting server..."
gunicorn mdpgroup.wsgi:application --bind "0.0.0.0:8000" --workers 4
