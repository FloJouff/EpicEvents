![Python](https://img.shields.io/badge/python-3.12.x-green.svg)
![Pytest](https://img.shields.io/badge/Pytest-8.2.x-blue.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLalchemy-2.0.x-red.svg)

# CRM System

## Overview

This project is a Customer Relationship Management (CRM) system built with Python, SQLAlchemy, and MySQL. The CRM system manages clients, contracts, events, and users, providing role-based access control and a secure authentication system.

## Features

- **User Management**: Create, update, delete, and authenticate users.
- **Role Management**: Define roles with specific permissions and assign them to users.
- **Client Management**: Manage clients (creating, updating, and deleting client records).
- **Contract Management**: Manage contracts associated with clients.
- **Event Management**: Manage events linked to contracts.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.11 or later
- MySQL
- Virtualenv

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/FloJouff/EpicEvents
cd crm
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
On Mac : `source venv/bin/activate`  
On Windows : ` venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Create a MySQL database and user for the CRM system. 

```sql
CREATE DATABASE 'name your db';
CREATE USER 'your admin user name' WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE 'name your db' TO 'your admin user name';
```

### 5. Configure a .env file

At the root of your project, create a .env file to store your database and jwt parameters 
# Connexion to db

```
DB_HOST=localhost
DB_PORT=3306
DB_NAME='name your db'
DB_USER='your admin user name'
DB_PASSWORD='yourpassword'

JWT_SECRET='yoursecretpassword'
JWT_REFRESH_SECRET=motdepassrefreshsecret
JWT_ALGORITHM =HS256 

SENTRY_KEY='your link to your sentry page'
```

### 6. Configure db for admin

Initialize Role model in database:

```bash
python initialize_role.py
```

Then create a superuser, Admin:

```bash
python create_admin.py
```

or

You can initialize your database with the sql file : Initialize.sql

### 7. Run the Application


finally, you can run the application:

```bash
python main.py
```

Using the crm is as easy as clicking on the command prompts in the various menus.
The menus displayed depend on the role of the logged-in user.


## Running Tests

To run the unit tests, use the following command:

```bash
python pytest
```

Ensure your MySQL database is set up correctly before running tests.

## Deployment

To deploy the CRM system, you can follow these general steps:

1. **Set Up the Server**: Install the necessary software (Python, MySQL, etc.) on your server.
2. **Clone the Repository**: Clone your project repository onto the server.
3. **Install Dependencies**: Use a virtual environment to install project dependencies.
4. **Configure Environment Variables**: Set up environment variables for production, such as database connection strings.
