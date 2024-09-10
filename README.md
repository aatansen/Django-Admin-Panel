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
    - [Excluding fields from forms](#excluding-fields-from-forms)
    - [Customizing list display](#customizing-list-display)
    - [Adding list view filters](#adding-list-view-filters)
    - [Implementing search functionality](#implementing-search-functionality)
    - [Making fields clickable in the list view](#making-fields-clickable-in-the-list-view)
    - [Enabling Inline editing in the list view](#enabling-inline-editing-in-the-list-view)
    - [Customizing model string representation](#customizing-model-string-representation)
    - [Setting meta options for admin models](#setting-meta-options-for-admin-models)
    - [Configuring default ordering](#configuring-default-ordering)

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
    admin.site.register(Membership_model,Membership_admin)
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
    admin.site.register(Membership_model,Membership_admin)
    ```

[⬆️ Go to top](#context)

#### Excluding fields from forms
- Using `exclude` in admin class
    ```py
    class Membership_admin(admin.ModelAdmin):
        exclude=('unique_code',)
    admin.site.register(Membership_model,Membership_admin)
    ```

[⬆️ Go to top](#context)

#### Customizing list display
- Using `list_display` in admin class
    ```py
    class Membership_admin(admin.ModelAdmin):
        list_display=['name','membership_plan','membership_active','unique_code']
    admin.site.register(Membership_model,Membership_admin)
    ```

[⬆️ Go to top](#context)

#### Adding list view filters
- Using `list_filter` in admin class
    ```py
    class Membership_admin(admin.ModelAdmin):
        list_display=['name','membership_plan','membership_active','unique_code']
        list_filter=["membership_plan"]
    admin.site.register(Membership_model,Membership_admin)
    ```

[⬆️ Go to top](#context)

#### Implementing search functionality
- Using `search_fields` in admin class
    ```py
    class Membership_admin(admin.ModelAdmin):
        search_fields=('name',)
        list_display=['name','membership_plan','membership_active','unique_code']
        list_filter=["membership_plan"]
    admin.site.register(Membership_model,Membership_admin)
    ```

[⬆️ Go to top](#context)

#### Making fields clickable in the list view
- Using `list_display_links` in admin class
    ```py
    class Membership_admin(admin.ModelAdmin):
        search_fields=('name',)
        list_display=['name','membership_plan','membership_active','unique_code']
        list_filter=["membership_plan"]
    admin.site.register(Membership_model,Membership_admin)
    list_display_links=['name','unique_code','membership_plan']
    ```

[⬆️ Go to top](#context)

#### Enabling Inline editing in the list view
- Using `list_editable` in admin class
    ```py
    class Membership_admin(admin.ModelAdmin):
        search_fields=('name',)
        list_display=['name','membership_plan','membership_active','unique_code']
        list_filter=["membership_plan"]
    admin.site.register(Membership_model,Membership_admin)
    list_editable=['membership_plan','unique_code']
    ```

[⬆️ Go to top](#context)

#### Customizing model string representation
- Adding `__str__` in model class
    ```py
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

        def __str__(self):
            return self.name
    ```

[⬆️ Go to top](#context)

#### Setting meta options for admin models
- Adding `Class Meta` in model class `verbose_name_plural`
    ```py
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

        def __str__(self):
            return self.name
        
        class Meta:
            verbose_name_plural='Gym Members'
    ```

[⬆️ Go to top](#context)

#### Configuring default ordering
- Adding `Class Meta` in model class `ordering`
    ```py
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

        def __str__(self):
            return self.name
        
        class Meta:
            verbose_name_plural='Gym Members'
            ordering=['name']
    ```

[⬆️ Go to top](#context)
