#!/bin/bash

echo "Collecting static files..."
python manage.py collectstatic --noinput || { echo "Failed to collect static files"; exit 1; }

echo "Making migrations..."
python manage.py makemigrations
python manage.py makemigrations accounts booking home notification || { echo "Failed to make migrations"; exit 1; }


echo "Applying migrations..."
python manage.py migrate
echo "Applying migrations for accounts app..."
python manage.py migrate accounts || { echo "Failed to apply migrations for accounts app"; exit 1; }
echo "Applying migrations for booking app..."
python manage.py migrate home || { echo "Failed to apply migrations for booking app"; exit 1; }
echo "Applying migrations for home app..."
python manage.py migrate booking || { echo "Failed to apply migrations for home app"; exit 1; }
echo "Applying migrations for notification app..."
python manage.py migrate notification || { echo "Failed to apply migrations for notification app"; exit 1; }
echo "All migrations applied successfully."

echo "Creating superuser..."
# python manage.py createsuperuser --noinput --username=admin --email=admin@gmail.com --password=admin || { echo "Failed to create superuser"; exit 1; }
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')" | python manage.py shell || { echo "Failed to create superuser"; exit 1; }

exec "$@"
