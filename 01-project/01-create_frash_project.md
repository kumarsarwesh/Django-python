cd 01-project/

# 1. Python check
python3 --version

# 2. Virtual environment create (IMPORTANT - missing tha)
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate   # (Linux/Mac)
# Windows me:
# venv\Scripts\activate

# 4. Django install
pip install django

# 5. Project create
django-admin startproject myproject

# 6. Project folder me jao
cd myproject

# 7. App create
python manage.py startapp myapp

# 8. Server run
python manage.py runserver


........................................

Commands to Run Project Next Day
cd 01-project/myproject

# Activate virtual environment
source venv/bin/activate   # (Linux/Mac)
# For Windows:
# venv\Scripts\activate

# Run the server
python manage.py runserver