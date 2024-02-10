FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PATH="/scripts:${PATH}"

WORKDIR /django
COPY . /django

RUN pip install --upgrade pip && pip install -r requirements.txt gunicorn
# RUN python manage.py collectstatic --noinput
# RUN python manage.py makemigrations
# RUN python manage.py migrate
# RUN python manage.py createsuperuser --noinput --username=admin --email=admin@gmail.com --password=admin

COPY ./scripts /scripts
RUN chmod +x /scripts/*

CMD ["/scripts/entrypoint.sh","gunicorn", "--bind", "0.0.0.0:8000", "flight_booking.wsgi:application"]
