# Foo Bar

A simple and interactive menu created using Django and Postgresql.

## Getting Started
Follow the instructions below to install the application on an Ubuntu machine for development purposes. For a runnung demo of the application, click on the link provided http://18.217.182.164:8000/menu/

### Prerequisites
```
sudo apt-get install python3 python3-pip postgresql virtualenv
```
### Create a Virtual Environment
Use the command below to create a virtual environment named 'myenv'
```
virtualenv -p python3 myenv
```
After the environment has been created, activate it using the following command.
```
source myenv/bin/activate
```
You will know that the virtual environment has started when you see (myenv) prefixed in front of your console.
### Clone the repository
Clone the codebase from Git using the following command.
```
git clone https://github.com/shraavanthp/foo_bar.git
```

### Create the database and user in PostgreSQL
Log into the interactive Postgres session using the command
```
sudo -u postgres psql
```
Enter the following commands to create a database and a user and grant the user all permissions.
```
postgres=# CREATE DATABASE foo_bar;
postgres=# CREATE USER testuser WITH PASSWORD 'password';
postgres=# GRANT ALL PRIVILEGES ON DATABASE foo_bar TO testuser;
```
Exit the postgres session by typing,
```
postgres=# \q
```
Edit the file foo_bar/'settings.py' to mention the username, password and database name.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'foo_bar',
        'USER': 'testuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
### Installing the prerequisites
At the project root, there is a file 'requirements.txt' that has all the dependancies required to be installed. Install them using the command.
```
pip3 install -U -r requirements.txt
```
### Migrate the tables
Enter the following command to migrate all the tables to the database.
```
python3 manage.py migrate
```
### Optional:
If you are running the application on a remote server, add the url of the server to the list of ALLOWED_HOSTS in the settings.py file.
```
ALLOWED_HOSTS = ['IP_ADDRESS']
```
### Get it running
Start the server using the command from the project root.
```
python3 manage.py runserver 0.0.0.0:8000
```
Access the application using the URL 'http://[IP_ADDRESS]:8000/menu'
