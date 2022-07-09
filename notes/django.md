---
id: bwga25jea7hw0yj0l3s1tuz
title: Django
desc: ''
updated: 1656410676687
created: 1655656138342
---
Django เป็น backend sever-side

## Django Workflow &rarr; MTV

- M = Model: data หรือ ข้อมูลที่จะแสดง
- V = View: ตัวจัดการ request ตามที่ user ขอมา
- T = Template: Text file เป็น HTML files และ Layout หรือ logic ที่จะ display data

## create virtual Environment

```Powershell
py -m venv "<name of project>"
```

## call virtual evironment

```Powershell
# On Windows using the Command Prompt:
"<name of project>"\Scripts\activate.bat

# On Windows using PowerShell: 
"<name of project>"\Scripts\Activate.ps1
```

## install Django

```Powershell
py -m pip install django
```

## check version

```Powershell
django-admin --version
```

## create Django project

```Powershell
django-admin startproject "<name of project>"
```

## run Django project

```Powershell
cd "<name of project>"
py manage.py runserver
```

## install app

```Powershell
py manage.py startapp "<name of app>"
```

## view

รับ HttpRequest

return HttpResponse

```python
#view.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")
```

สร้าง urls.py

```python
#urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
```

ทำเหมือนกันใน myapp

```python
#urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('members/', include('members.urls')),
    path('admin/', admin.site.urls)
]
```
