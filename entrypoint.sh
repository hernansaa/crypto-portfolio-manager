#!/bin/sh

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the Gunicorn server
gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3
