Django Project Setup Summary
First Time Setup
1. Go to Project Folder
cd 01-project

2. Check Python Version
python --version

or

python3 --version
3. Create Virtual Environment
python -m venv venv

or

python3 -m venv venv
4. Activate Virtual Environment

Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate

After activation you should see:

(venv)

at the beginning of the terminal line.

5. Install Django
pip install django

6. Create Django Project
django-admin startproject myproject

7. Enter Project Folder
cd myproject

8. Create App
python manage.py startapp myapp

9. Run Server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/