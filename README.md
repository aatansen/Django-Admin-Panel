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
