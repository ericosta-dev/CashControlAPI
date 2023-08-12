# Django REST Framework Project

This is a README for a Django REST Framework project. In this project, we're using Python and the Django REST Framework to build an API, and PostgreSQL as our database.

## Prerequisites
For the correct setup of the project, make sure you have the following installed on your system:

-   Python 3. 8+
-   Pip (Python Package Installer)
-   Virtualenv
-   PostgreSQL

## Project Setup
Follow the below instructions to get the project up and running.

### Step 1: Clone the Project
Clone the project from our repository into your local machine.

Using ssh
```bash
git clone git@github.com:ericosta-dev/CashControlAPI.git
```

Using https
```bash
git clone https://github.com/ericosta-dev/CashControlAPI.git
```

### Step 2: Create a Virtual Environment
Create a virtual environment for the project using the following command:
```bash
python -m venv venv
source venv/bin/activate
```

### Step 3: Install the Project Dependencies
Install the project dependencies using the following command:
```bash
pip install -r requirements.txt
```

### Step 4: Environment Variables
Create a .env file in the root directory of the project and add the following environment variables:
```bash
SECRET_KEY=secret_key
DEBUG=True
NAME=dbcashcontrol
USER=dbuser
PASSWORD=dbpassword
HOST=localhost
PORT=5432
```

### Step 5: Run the Project
Run the project using the following command:
```bash
python manage.py runserver
```

The project will be available at http://localhost:8000
