1.  django-admin startproject myproject
cd myproject
python manage.py startapp myapp


myproject
│
├── manage.py
├── db.sqlite3
├── myproject
│     ├── settings.py
│     ├── urls.py
│     └── ...
│
└── myapp
      ├── models.py
      ├── views.py
      ├── urls.py
      ├── templates
      │      └── index.html
      └── migrations




 2. Register App
File: myproject/settings.py

Add:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'myapp',
]     



3. Create Model
File: myapp/models.py
from django.db import models

class Person(models.Model):
    username = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.username
4. Create Database Table

Run:

python manage.py makemigrations
python manage.py migrate

This creates table:

myapp_person

inside db.sqlite3.



5. Create View
File: myapp/views.py

from django.shortcuts import render
from .models import Person

def home(request):

    msg = ""

    if request.method == "POST":

        username = request.POST['username']
        city = request.POST['city']

        Person.objects.create(
            username=username,
            city=city
        )

        msg = "Data Saved Successfully"

    persons = Person.objects.all()

    return render(request, "index.html", {
        "msg": msg,
        "persons": persons
    })


6. Create App URLs
File: myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
]


7. Connect App URLs to Project
File: myproject/urls.py
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]


8. Create Template Folder

Inside myapp, create:

myapp
│
├── templates
│     └── index.html



9. Create HTML Form
File: myapp/templates/index.html


<!DOCTYPE html>
<html>
<head>
    <title>Django Form</title>
</head>
<body>

<h2>Add Person</h2>

<form method="POST">

    {% csrf_token %}

    Username:
    <input type="text" name="username">

    <br><br>

    City:
    <input type="text" name="city">

    <br><br>

    <button type="submit">
        Save
    </button>

</form>

<h3>{{msg}}</h3>

<hr>

<h2>Saved Data</h2>

<table border="1">

<tr>
    <th>Username</th>
    <th>City</th>
</tr>

{% for person in persons %}

<tr>
    <td>{{person.username}}</td>
    <td>{{person.city}}</td>
</tr>

{% endfor %}

</table>

</body>
</html>



10. Run Server
python manage.py runserver

Open:

http://127.0.0.1:8000/myapp/
Data Flow
Browser
   ↓
index.html
   ↓
POST Request
   ↓
views.py
   ↓
Person.objects.create()
   ↓
models.py
   ↓
SQLite Database (db.sqlite3)
   ↓
Person.objects.all()
   ↓
views.py
   ↓
index.html
   ↓
Display Table