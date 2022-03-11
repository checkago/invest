#!/bin/sh


python manage.py migrate --run-syncdb

gunicorn invest.wsgi:application --bind 0.0.0.0:8000 --reload  -w 4
