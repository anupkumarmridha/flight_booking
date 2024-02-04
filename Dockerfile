FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PATH="/scripts:${PATH}"

WORKDIR /django
COPY . /django

RUN pip install --upgrade pip && pip install -r requirements.txt gunicorn


COPY ./scripts /scripts
RUN chmod +x /scripts/*

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "flight_booking.wsgi:application"]