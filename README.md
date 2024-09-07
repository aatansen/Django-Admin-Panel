<div align="center">
<h1>Django Admin Panel</h1>
</div>

## Context
- [Preparation](#preparation)
- [Django Admin](#django-admin)
- [Database](#database)
    - [Relational Database](#relational-database)
    - [Non-Relational Database](#non-relational-database)
    - [How does database work?](#how-does-database-work)
- [What is Django model?](#what-is-django-model)
    - [Creating Django model](#creating-django-model)
    - [Different approaches to register model](#different-approaches-to-register-model)
- [Django Admin Panel](#django-admin-panel)
    - [Managing user and group visibility](#managing-user-and-group-visibility)
    - [Creating object](#creating-object)
    - [Viewing, Updating & Deleting object](#viewing-updating--deleting-object)
    - [Customizing admin titles](#customizing-admin-titles)
    - [Configuring field display](#configuring-field-display)
    - [Customizing field layouts as Inline rows](#customizing-field-layouts-as-inline-rows)

### Preparation
- Create project 
    - `django-admin startproject admin_project .`
- Create app
    - `py manage.py startapp admin_app`
- Register app `admin_app` in `INSTALLED_APPS`

[⬆️ Go to top](#context)

### Django Admin
- Django Admin is a powerful tool that allows developers to manage database content through a web-based interface 
- It is automatically generated and customizable which makes it easy to configure for different kinds of applications 
- It provides CRUD (Create, Read, Update, Delete) operations out of the box for database models 
- Security features are built-in, including user authentication and permissions management 

[⬆️ Go to top](#context)

### Database
- A database is simply an organized collection of data 
- By default, we use an SQLite database engine in our Django applications (which is automatically configured, once we create and run our Django project) 
- Databases are classified as either relational or non-relational databases 
- Once data is stored in a database, we as the developer can then manipulate and query the data in the database for our own unique use case 

[⬆️ Go to top](#context)

#### Relational Database
- A relational database is organized into tables that consist of rows and columns
- Each row represents a particular record, and each column represents a field 
- To query and manipulate data in a relational database you will need to use SQL (Structured Query Language) 

[⬆️ Go to top](#context)

#### Non-Relational Database
- A non-relational database or NOSQL database is another type of database, but these types do not use the traditional table-based relational structure 
- Non-relational databases instead use data models such as key-value, column-family and document 
- It is popular for handling large-scale, distributed and undistributed data 

[⬆️ Go to top](#context)

#### How does database work?
- A diagram of database
    ```mermaid
    sequenceDiagram
        participant User
        participant Form
        participant Server
        participant Database

        User->>Form: Fill out and submit form
        Form->>Server: Send form data
        Server->>Server: Validate data
        alt Data Valid
            Server->>Database: Save data
            Database-->>Server: Confirmation
            Server->>Form: Send confirmation to User
        else Data Invalid
            Server->>Form: Send error message to User
        end
    ```

[⬆️ Go to top](#context)

### What is Django model?
- A Django model is a built-in feature used by Django to create database tables 
along with their fields, and additional constraints that need be included
- Django models are essentially Python classes that represent database tables
- Moreover, a Django model class is defined in a file called models.py. Each attribute 
of the model class represents a field in the corresponding database table

[⬆️ Go to top](#context)

#### Creating Django model
- In `models.py` create python class
    ```py
    from django.db import models

    # Create your models here.
    class Membership_model(models.Model):
        name=models.CharField(max_length=500)
        MEMBERSHIP_CHOICES=(
            ('s','Standard'),
            ('p','Premium'),
            ('ux','Ultimate Deluxe'),
        )
        membership_plan=models.CharField(max_length=2,choices=MEMBERSHIP_CHOICES)
        membership_active=models.BooleanField(default=True)
        unique_code=models.CharField(max_length=250)
    ```
- Migrate Database
    - `py manage.py makemigrations`
    - `py manage.py migrate`

- Register model in `admin.py`
    ```py
    from django.contrib import admin
    from models import *

    # Register your models here.
    admin.site.register(Membership_model)
    ```
- Create superuser to view the model in Django Admin Panel
    - `py manage.py createsuperuser`
- Now login to Django admin to view the created model

[⬆️ Go to top](#context)

#### Different approaches to register model
- Creating a class to modify admin and register
    ```py
    from django.contrib import admin
    from .models import *

    # Register your models here.
    class Membership_admin(admin.ModelAdmin):
        pass
    admin.site.register(Membership_model,Membership_admin)
    ```
- Using decorator
    ```py
    from django.contrib import admin
    from .models import *

    # Register your models here.
    @admin.register(Membership_model)
    class Membership_admin(admin.ModelAdmin):
        pass
    ```

[⬆️ Go to top](#context)

### Django Admin Panel
#### Managing user and group visibility
- We can unregister a model
    ```py
    from django.contrib.auth.models import User,Group

    admin.site.unregister(User)
    admin.site.unregister(Group)
    ```

[⬆️ Go to top](#context)

#### Creating object
- By navigating to admin panel we can add new object of our created model `Membership_model`

#### Viewing, Updating & Deleting object
- Opening the created object we can do these operation

[⬆️ Go to top](#context)

#### Customizing admin titles
- By changing site header
    ```py
    # Customizing admin titles
    admin.site.site_header="Admin Panel"
    ```
- To change website title page
    ```py
    admin.site.index_title='Admin'
    admin.site.site_title='Panel Practice'
    ```
[⬆️ Go to top](#context)

#### Configuring field display
- In the class we can define fields 
    ```py
    class Membership_admin(admin.ModelAdmin):
    fields=(
        'name',
        'membership_plan',
        'membership_active',
    )
    ```

[⬆️ Go to top](#context)

#### Customizing field layouts as Inline rows
- By adding field name in one tuple
    ```py
    class Membership_admin(admin.ModelAdmin):
        fields=(
            ('name','membership_plan'),
            'membership_active',
        )
    ```

[⬆️ Go to top](#context)
