cd 01-project/
python3 --version
source venv/bin/activate
pip install django
django-admin startproject myproject .
python manage.py startapp myapp
python manage.py runserver
