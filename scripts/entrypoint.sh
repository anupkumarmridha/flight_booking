#!/bin/bash

echo "Collecting static files..."
python manage.py collectstatic --noinput || { echo "Failed to collect static files"; exit 1; }

echo "Making migrations..."
python manage.py makemigrations accounts booking home notification || { echo "Failed to make migrations"; exit 1; }
echo "Applying migrations..."
python manage.py migrate accounts booking home notification || { echo "Failed to apply migrations"; exit 1; }
echo "Creating superuser..."
# python manage.py createsuperuser --noinput --username=admin --email=admin@gmail.com --password=admin || { echo "Failed to create superuser"; exit 1; }
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')" | python manage.py shell || { echo "Failed to create superuser"; exit 1; }

exec "$@"
