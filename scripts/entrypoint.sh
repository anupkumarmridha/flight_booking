#!/bin/bash

echo "Collecting static files..."
python manage.py collectstatic --noinput || { echo "Failed to collect static files"; exit 1; }
echo "Making migrations..."
python manage.py makemigrations || { echo "Failed to make migrations"; exit 1; }
echo "Applying migrations..."
python manage.py migrate || { echo "Failed to apply migrations"; exit 1; }
echo "Creating superuser..."
python manage.py createsuperuser --noinput --username=admin --email=admin@gmail.com --password=admin || { echo "Failed to create superuser"; exit 1; }
exec "$@"
