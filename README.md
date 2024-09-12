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
- [Django Admin Configuration](#django-admin-configuration)
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
    - [Implementing change list actions / Adding custom actions](#implementing-change-list-actions--adding-custom-actions)
- [Enhancing Django Admin Functionality](#enhancing-django-admin-functionality)
    - [Configure a Django app](#configure-a-django-app)
    - [Introduction to foreign keys & Model Creation](#introduction-to-foreign-keys--model-creation)
    - [Integrating pre-populated fields](#integrating-pre-populated-fields)
    - [Using Inline models for related data](#using-inline-models-for-related-data)
    - [Custom Methods List Display](#custom-methods-list-display)
- [Comprehensive Admin Management](#comprehensive-admin-management)
    - [Organizing admin forms with fieldsets](#organizing-admin-forms-with-fieldsets)
    - [Alter the HTML structure of the login page](#alter-the-html-structure-of-the-login-page)
    - [Enhancing admin with CSS overrides](#enhancing-admin-with-css-overrides)
    - [Manual user permissions configuration](#manual-user-permissions-configuration)
    - [Code-based user permissions configuration](#code-based-user-permissions-configuration)
    - [Custom messages based on permissions](#custom-messages-based-on-permissions)
    - [Managing multiple admin sites](#managing-multiple-admin-sites)
- [Third-party Tools](#third-party-tools)
    - [Adding CAPTCHA protection](#adding-captcha-protection)
    - [Distinguishing development environments](#distinguishing-development-environments)

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

### Django Admin Configuration
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

#### Implementing change list actions / Adding custom actions
- Adding `Class Meta` in model class `ordering`
    ```py
    class Membership_admin(admin.ModelAdmin):
        search_fields=('name',)
        list_display=['name','membership_plan','membership_active','unique_code']
        list_filter=["membership_plan"]

        # Custom action
        actions=('set_membership_to_active',)
        def set_membership_to_active(self,request,queryset):
            queryset.update(membership_active=True)
            self.message_user(request,'Membership activated successfully')
        set_membership_to_active.short_description='Mark to set membership active'
    admin.site.register(Membership_model,Membership_admin)
    ```

[⬆️ Go to top](#context)

### Enhancing Django Admin Functionality
#### Configure a Django app
- Create an app `edu_app`
    - `py manage.py startapp edu_app`
- Add app in `INSTALLED_APPS`

[⬆️ Go to top](#context)

#### Introduction to foreign keys & Model Creation
- A database schema with two tables: `Course_model` & `Lecture_model`
    ```mermaid
    erDiagram
        Course_model {
            course_title STRING
            course_description TEXT
            slug STRING
        }
        
        Lecture_model {
            lecture_name STRING
            slug STRING
            course INT FK "Foreign Key"
        }
        
        Course_model ||--o{ Lecture_model : has
    ```
- Create two model `Course_model` & `Lecture_model` with those field in `edu_app`

[⬆️ Go to top](#context)

#### Integrating pre-populated fields
- In `admin.py` we can re-populate fields using `prepopulated_fields`
    ```py
    class Course_admin(admin.ModelAdmin):
        prepopulated_fields={
            'slug':('course_title',)
        }
    admin.site.register(Course_model,Course_admin)

    class Lecture_admin(admin.ModelAdmin):
        prepopulated_fields={
            'slug':('lecture_name',)
        }
    admin.site.register(Lecture_model,Lecture_admin)
    ```

[⬆️ Go to top](#context)

#### Using Inline models for related data
- By using `StackedInline` or `TabularInline`
    ```py
    class Inline_lecture(admin.StackedInline):
        model=Lecture_model
        # extra=2
        max_num=2

    class Course_admin(admin.ModelAdmin):
        inlines=[Inline_lecture]
        prepopulated_fields={
            'slug':('course_title',)
        }
    admin.site.register(Course_model,Course_admin)

    class Lecture_admin(admin.ModelAdmin):
        prepopulated_fields={
            'slug':('lecture_name',)
        }
    admin.site.register(Lecture_model,Lecture_admin)
    ```
    - This will allow to add multiple lecture data while adding a perticular course

[⬆️ Go to top](#context)

#### Custom Methods List Display
- Creating custom heading 
    ```py
    class Course_admin(admin.ModelAdmin):
        list_display=['course_title','course_description','Course_heading']
        
        def Course_heading(self,obj):
            return obj.course_title + " - " + obj.course_description
    admin.site.register(Course_model,Course_admin)
    ```

[⬆️ Go to top](#context)

### Comprehensive Admin Management
#### Organizing admin forms with fieldsets
- Using `fieldsets`
    ```py
    class Lecture_admin(admin.ModelAdmin):
        # fields=('lecture_name','course','slug')
        fieldsets=(
            ('Lecture:',{
                'fields':('lecture_name','slug'),
                'description':'lecture details',
            }),
            ('Course:',{
                'fields':('course',),
                'description':'Course linked',
            }),
        )
        prepopulated_fields={
            'slug':('lecture_name',)
        }
    admin.site.register(Lecture_model,Lecture_admin)
    ```

[⬆️ Go to top](#context)

#### Alter the HTML structure of the login page
- Define `STATIC_ROOT` in `settings.py`
    ```py
    STATIC_ROOT=os.path.join(BASE_DIR,'static')
    ```
- Set static url in `urls.py`
    ```py
    from django.conf.urls.static import static
    from django.conf import settings
    urlpatterns = [
        path('admin/', admin.site.urls),
    ]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    ```
- Execute the `collectstatic` command
    - `py manage.py collectstatic`
- Set `TEMPLATES`'s `DIRS`
    ```py
    'DIRS': [os.path.join(BASE_DIR,'templates')],
    ```
- Now get the content of the admin login from django package
    - `\env\Lib\site-packages\django\contrib\admin\templates\admin\login.html"`
- Create `templates` directory with `admin` subdirectory and put `login.html` there
- Now in `admin.py` create a class and define `login_template`
    ```py
    class Admin_login_area(admin.AdminSite):
        login_template='admin/login.html'
    ```

[⬆️ Go to top](#context)

#### Enhancing admin with CSS overrides
- Set `STATICFILES_DIRS` and comment out `STATIC_ROOT`
    ```py
    STATIC_URL = 'static/'
    # STATIC_ROOT=os.path.join(BASE_DIR,'static')
    STATICFILES_DIRS=[BASE_DIR / 'static']
    ```
- Now modify any css for example `login.css` which is in `static` directory after `collectstatic` command
- Hard refresh in admin site to see the changes

[⬆️ Go to top](#context)

#### Manual user permissions configuration
- Login to admin and create a new user with active & staff permissions
- Now give permission to that user as necessary

[⬆️ Go to top](#context)

#### Code-based user permissions configuration
- Go to `admin.py` and set permission
    ```py
    class Membership_admin(admin.ModelAdmin):
        def has_add_permission(self, request):
            return False
        
        def has_change_permission(self, request, obj=None):
            return False
        
        def has_delete_permission(self, request, obj=None):
            return False
    admin.site.register(Membership_model,Membership_admin)
    ```

[⬆️ Go to top](#context)

#### Custom messages based on permissions
- In `admin.py` model admin where methods are defined, we can add custom messages to show in admin site
    ```py
    from django.contrib import messages
    class Membership_admin(admin.ModelAdmin):
        def has_delete_permission(self, request, obj=None):
            if obj!=None and request.POST.get('action')=='delete_selected':
                messages.add_message(request,messages.ERROR,(
                    "Are you sure you want to delete this?"
                ))
            return True
    admin.site.register(Membership_model,Membership_admin)
    ```

[⬆️ Go to top](#context)

#### Managing multiple admin sites
- Create admin model class in `admin.py` and register model
    ```py
    class Edu_admin_site(admin.AdminSite):
        site_header="Education Admin"
    edu_site=Edu_admin_site()
    edu_site.register(Course_model)
    edu_site.register(Lecture_model)
    ```
- Set url in `urls.py`
    ```py
    from edu_app.admin import edu_site
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('edu-admin/', edu_site.urls),
    ]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    ```
> [!WARNING]
> `?: (urls.W005) URL namespace 'admin' isn't unique. You may not be able to reverse all URLs in this namespace`

- To solve this warning set `name` argument
    ```py
    class Edu_admin_site(admin.AdminSite):
        site_header="Education Admin"
    edu_site=Edu_admin_site(name='edu_site')
    edu_site.register(Course_model)
    edu_site.register(Lecture_model)
    ```

[⬆️ Go to top](#context)

### Third-party Tools
#### Adding CAPTCHA protection
- Install [django-multi-captcha-admin](https://pypi.org/project/django-multi-captcha-admin/)
- Also install `pillow` as the captcha contain images
- Add `multi_captcha_admin` to your `INSTALLED_APPS` setting before `django.contrib.admin` app
    ```py
    INSTALLED_APPS = [
        'multi_captcha_admin',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'admin_app',
        'edu_app',
    ]
    ```
- Now there are `simple-captcha`,`recaptcha` & `recaptcha2`. We are going to implement `simple-captcha`
- Go to [simple-captcha docs](https://django-simple-captcha.readthedocs.io/en/latest/) and follow the installation and setup
    - Install `django-simple-captcha`
        - `pip install  django-simple-captcha`
    - Add `captcha` to the `INSTALLED_APPS` in `settings.py`
    - Run `py manage.py migrate`
- Add `captcha/` route in `urls.py`:
    ```py
    urlpatterns += [
        path('captcha/', include('captcha.urls')),
    ]
    ```
- Now to make sure it work correctly we have to remove `Admin_login_area` class where we modified `login.html` and delete `login.html` from `templates` directory
    ```py
    class Admin_login_area(admin.AdminSite):
        login_template='admin/login.html'
    ```
- Now rerun the server to see the captcha

[⬆️ Go to top](#context)

#### Distinguishing development environments
- Install [django-admin-env-notice](https://pypi.org/project/django-admin-env-notice/)
    - `pip install django-admin-env-notice`
- Add `django_admin_env_notice` to `INSTALLED_APPS` before `django.contrib.admin`
    ```py
    INSTALLED_APPS = [
        'django_admin_env_notice',
        'multi_captcha_admin',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'admin_app',
        'edu_app',
        'captcha',
    ]
    ```
- Add context processor
    ```py
    TEMPLATES = [
        {
            ...
            'OPTIONS': {
                "context_processors": [
                    ...
                    "django_admin_env_notice.context_processors.from_settings",
                ],
            },
        },
    ]
    ```
- Now Set label and color for current environment
    ```py
    # Env settings
    ENVIRONMENT_NAME = "Development server"
    ENVIRONMENT_COLOR = "#40E0D0"
    ENVIRONMENT_FLOAT = True
    ENVIRONMENT_SHOW_TO_UNAUTHENTICATED = False
    ```

[⬆️ Go to top](#context)