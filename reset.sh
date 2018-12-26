#!/bin/sh

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

rm -rf db.sqlite3
rm -rf figures

python manage.py makemigrations
python manage.py migrate
python manage.py init 
python manage.py runserver