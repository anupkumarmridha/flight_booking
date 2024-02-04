#!/bin/bash

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --noinput --username=admin --email=admin@gmail.com --password=admin