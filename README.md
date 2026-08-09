# 🐍 Django Project Setup Guide — Windows 11

A step-by-step guide for setting up a **Django project with Python >= 3.12 ** on **Windows 11** using Command Prompt or PowerShell.

> **💡 Environment:** Windows 11
> **🐍 Python:** 
> **📁 Project location:** Directly under `C:\`
> **🌐 Development server:** `http://127.0.0.1:8000/`

---

## 📋 Prerequisites

All commands in this guide are intended for:

* 🪟 Windows 11
* 💻 Command Prompt (`cmd`) or PowerShell
* 🐍 Python 
* 📁 A project located directly under `C:\`

For example:

```text
C:\myproject
```

---

# 1. 🐍 Install Python

## 1.1 Download Python

Go to the official Python website:

**https://www.python.org/downloads/windows/**

Download the latest **Python  Windows installer (64-bit)**.

## 1.2 Install Python

Run the installer.

> ⚠️ **IMPORTANT:** Before clicking **Install Now**, make sure you check:
>
> ☑️ **Add python.exe to PATH**

Then click:

**Install Now**

## 1.3 Verify the installation

After installation, open a **new Command Prompt or PowerShell** window.

Run:

```powershell
python --version
```

You should see something similar to:

```text
Python 
```

You can also verify Python 3.12 specifically using the Python Launcher:

```powershell
py -3.12 --version
```

## 1.4 Upgrade pip

Upgrading `pip` is recommended:

```powershell
python -m pip install --upgrade pip
```

---

# 2. 📁 Create the Project Folder

## 2.1 Open Command Prompt or PowerShell

Open either:

* Command Prompt (`cmd`)
* PowerShell

## 2.2 Go to the `C:\` drive

```powershell
cd C:\
```

## 2.3 Create the project folder

Choose any project name. For this example, we'll use `myproject`.

```powershell
mkdir myproject
cd myproject
```

Your current directory should now be:

```text
C:\myproject
```

---

# 3. 🫙 Create and Activate Virtual Environment

Using a virtual environment keeps your project's Python packages isolated from other projects.

## 3.1 Create the virtual environment

Create a virtual environment named `.venv`:

```powershell
python -m venv .venv
```

This creates:

```text
C:\myproject\.venv
```

## 3.2 Activate the virtual environment

### Command Prompt (`cmd`)

```cmd
.venv\Scripts\activate.bat
```

### PowerShell

```powershell
.venv\Scripts\Activate.ps1
```


> **Note:** Linux/macOS activation is not required for this Windows guide.
For Linux/MacOS:
```bash      
source .venv/bin/activate
```

## 3.3 Verify activation

After activation, `(.venv)` should appear at the beginning of your terminal prompt:

```text
(.venv) C:\myproject>
```

---

# 4. 🦄 Install Django

Make sure the virtual environment is activated.

Install the latest stable Django release:

```powershell
pip install django
```

or

```powershell
python -m pip install django
```

Verify the installation:

```powershell
python -m django --version
```

---

> **Note:** Project Requirements. 
If project has requirements.txt file then install all project package and dependendencies.

```poweshell
pip install -r requirements.txt
```

---

# 5. 📦 Create the Django Project

## 5.1 Make sure you are in the project directory

You should be inside:

```text
C:\myproject
```

And your virtual environment should be activated.

## 5.2 Create the Django project

For this example, the Django project configuration will be named `config`:

```powershell
django-admin startproject config .
```

> 💡 **Important:** The dot (`.`) at the end is intentional.
>
> It tells Django to create the project in the **current directory** instead of creating an additional nested `config` folder.

## 5.3 Project structure

Your folder should now look similar to:

```text
C:\myproject\
│
├── .venv\
│
├── config\
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── manage.py
```

---

# 6. 📦 Create a Django App

Create an application inside the project.

For this example, we'll use the name `core`:

```powershell
python manage.py startapp core
```

You can use another name, such as:

* `blog`
* `accounts`
* `products`
* `shop`
* `core`

After creating the app, the structure will look approximately like:

```text
C:\myproject\
│
├── .venv\
├── config\
├── core\
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations\
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
└── manage.py
```

---

# 7. ⚙️ Configure `settings.py`

Open:

```text
C:\myproject\config\settings.py
```

The following configuration sets up:

* 📄 Global templates
* 🎨 Static files
* 🖼️ Media/uploaded files
* 📦 The `core` application

---

## 7.1 Verify `BASE_DIR`

Django normally creates this automatically.

Make sure you have:

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
```

---

## 7.2 Add the Django App

Find `INSTALLED_APPS` and add `core`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core',
]
```

> 💡 If you named your app something other than `core`, replace `'core'` with your app name.

---

## 7.3 Configure Templates

Find the `TEMPLATES` configuration and update `DIRS`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

This allows you to keep project-wide templates in:

```text
C:\myproject\templates\
```

## 7.4 Create the templates folder

From:

```text
C:\myproject
```

run:

```powershell
mkdir templates
```

---

# 8. 🎨 Configure Static Files

Static files include:

* CSS
* JavaScript
* Images used by your website
* Fonts
* Other frontend assets

Add or update these settings, usually near the bottom of `settings.py`:

```python
STATIC_URL = 'static/'

# Used by collectstatic in production
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Project-level static files
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

## 8.1 Create the static folder

From `C:\myproject`:

```powershell
mkdir static
```

Your project will now have:

```text
C:\myproject\
├── static\
├── templates\
├── core\
├── config\
└── manage.py
```

---

# 9. 🖼️ Configure Media Files

Media files are files uploaded by users, such as:

* Profile pictures
* Product images
* Documents
* Other uploaded files

Add the following to `settings.py`:

```python
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## 9.1 Create the media folder

From `C:\myproject`:

```powershell
mkdir media
```

---

# 10. 🌐 Configure URLs

Open:

```text
C:\myproject\config\urls.py
```

Use the following configuration:

```python
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]


# Add static and media URLS if in development.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

> 💡 Django's development server automatically handles files from `STATICFILES_DIRS` when `django.contrib.staticfiles` is enabled and `DEBUG=True`, so you normally do **not** need to add `STATIC_URL` manually here.

---

# 11. 🔗 Create `core/urls.py`

Because `config/urls.py` includes:

```python
path('', include('core.urls')),
```

you need to create a URL configuration for the `core` app.

Create this file:

```text
C:\myproject\core\urls.py
```

Add:

```python
from django.urls import path

from . import views


urlpatterns = [
    # Add your application URLs here.
]
```

You can add views later, for example:

```python
path('', views.home, name='home'),
```

---

# 12. 🗄️ Run Database Migrations

Make sure:

* ✅ You are inside `C:\myproject`
* ✅ `.venv` is activated

Run:

```powershell
python manage.py makemigrations
python manage.py migrate
```

The `migrate` command creates the initial Django database tables.

---

# 13. 👤 Create a Superuser

Creating a superuser is optional, but recommended if you want to use the Django Admin interface.

Run:

```powershell
python manage.py createsuperuser
```

Follow the prompts to enter:

* Username
* Email address
* Password

After starting the server, you can access the admin panel at:

```text
http://127.0.0.1:8000/admin/
```

---

# 14. 🚀 Run the Development Server

Make sure your virtual environment is activated.

Run:

```powershell
python manage.py runserver
```

You should see output similar to:

```text
Starting development server at http://127.0.0.1:8000/
```

Open your browser and visit:

**http://127.0.0.1:8000/**

🎉 Your Django development server is now running!

---

# 15. 📁 Final Project Structure

At this point, your project should look approximately like this:

```text
C:\myproject\
│
├── .venv\
│
├── config\
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core\
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations\
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── media\
│
├── static\
│
├── staticfiles\
│   
│
├── templates\
│
└── manage.py

```

---

# ⚡ Quick Command Reference

Once Python is installed, the main setup commands are:

```powershell
# Go to C:\
cd C:\

# Create and enter project folder
mkdir myproject
cd myproject

# Create virtual environment
python -m venv .venv

# Activate on PowerShell
.venv\Scripts\Activate.ps1

# Activate on Command Prompt
.venv\Scripts\activate.bat

# Upgrade pip
python -m pip install --upgrade pip

# Install Django
python -m pip install django

# Create Django project
django-admin startproject config .

# Create Django app
python manage.py startapp core

# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

---


# ✅ Setup Checklist

Use this checklist to verify your environment:

* [ ] 🐍 Python installed
* [ ] 🔧 Python added to PATH
* [ ] 📦 pip upgraded
* [ ] 📁 Project created under `C:\`
* [ ] 🧪 `.venv` created
* [ ] ✅ Virtual environment activated
* [ ] 🦄 Django installed
* [ ] 🏗️ Django project created
* [ ] 📦 Django app created
* [ ] ⚙️ `settings.py` configured
* [ ] 📄 `templates` folder created
* [ ] 🎨 `static` folder created
* [ ] 🖼️ `media` folder created
* [ ] 🔗 `core/urls.py` created
* [ ] 🗄️ Database migrations applied
* [ ] 👤 Superuser created (optional)
* [ ] 🚀 Development server running
* [ ] 🌐 `http://127.0.0.1:8000/` accessible

---


😀 Happy coding!

