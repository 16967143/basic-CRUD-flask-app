# Basic CRUD flask app for managing employees
Basic CRUD (Create, Read, Update, Delete) employee management web app built in Python & Flask, **loosely** based off the [scotch.io tutorial]( https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one).

![home page screenshot](screenshots/home-page-screenshot.png)
![home page screenshot2](screenshots/home-page-screenshot2.png)
![employees screenshot](screenshots/employees-screenshot.png)

## Stack information
The app is written in Python on top of the Flask micro-framework. The front-end was built with Semantic-UI, an easy to use HTML, CSS and JS front-end library that looks clean out the box.
PostgreSQL was implemented as the database of choice, in conjunction with the SQLAlchemy ORM to simplify CRUD operations. Alembic is used for making migrations to the database model.

Some adjustments and custom code have been applied to the styling and javascript components of the app to make for a clean and simple UX. The custom look and feel of the app was also 
achieved by designing and adding a series of custom logos, fonts and images. A working name for the app is *DataBae*, as emobodied by the logos. 

## List of features
The following are the main high-level features available through the app:

* Users can register and login as employees.
* Administrators can create, update, and delete departments and roles.
* Administrators can assign employees to a department and assign them roles.
* Administrators view all employees and their details.
* Standard (non-admin) users have access to a "Dashboard" (the contents of which have been left empty for this iteration of the app).
* Admin users have access to an "Admin Dashboard" (the contents of which have been left empty for this iteration of the app).
* Helpful error, warning and success messages help the user to navigate effectively throughout form completion stages of the app.

## How to use use this repo
The main purpose of this repo is to put in place a working template for a simple CRUD app which can be built upon as necessary for particular applications.
That is to say, the app is not "complete" in the sense that it does not really perform a useful function as-is. Rather, it lays the ground work for building useful 
applications by addressing a fairly broad range of tasks which are common between most apps. 

The suggested workflow for building an app with this template is the following:
1. Fork this repo and rename it to something appropriate
1. Read "Instructions for development" below (modify as necessary for your app)
1. Develop your app!

## Instructions for development
To start your app for development or demonstration, first follow "Setup and installation" the first time the app is to be run. Thereafter, refer to the "Running the app" section eah time the app
is to be run.

### Setup and installation
Clone the repository:

    git clone https://github.com/16967143/basic-CRUD-flask-app.git
    
Set up a [conda](https://conda.io/miniconda.html) environment (or alternatively use virtual-env):

    cd basic-CRUD-flask-app
    conda create -y -n crud-app --file conda_environment.txt python=3.6
    source activate crud-app
    pip install -r requirements.txt
    
Initialise the PostgreSQL database:
    
    initdb -D PGDATA  # creates a new "database cluster"
    createdb dreamteam_db  # creates a new database "dreamteam_db" within the db cluster
    pgctl -D PGDATA -l dreamteam_db_logfile.log start  # starts a background postgres daemon
    psql dreamteam_db  # starts the interactive pg console
    
Add user privileges to the database (NB: make sure to modify these passwords):
    
    CREATE USER admin WITH SUPERUSER PASSWORD 'admin';
    CREATE USER root WITH SUPERUSER PASSWORD '';
    
Set up your local app instance by creating the following...

    mkdir instance
    touch instance/config.py
    
...and adding the following settings to the instance/config.py file and save the changes:

    SECRET_KEY = 's0m3Rand0mSecretKeyOfY0urChoicE!'
    SQLALCHEMY_DATABASE_URI = 'postgres://admin:[admin]@localhost/dreamteam_db'  # Note: replace '[admin]' with the admin password chosen above
    
Run the database migrations:

    flask db upgrade
        
The app is now ready to run! 
    
### Running the app
The following steps should be performed each time the app is run.

Activate your app's conda environment:

    cd [path to app]
    source activate crud-app
    
Start the database daemon:

    pgctl -D PGDATA -l dreamteam_db_logfile.log start  # Note: to check that it is running as a process you can use the 'ps' command

Define the following environment variables:

    export FLASK_CONFIG=development
    export FLASK_APP=run.py
    
Run the app:

    flask run
    
The app can now be accessed by visiting [127.0.0.1:5000](127.0.0.1:5000) in your browser. It is recommended to use Firefox
as the app has not yet been optimised for Chrome (and IE, if that wasn't already assumed). 

### Further development notes

#### Database migrations
It is important to note that every time changes are made to the database models in the python code base, the database needs 
to be updated to reflect these changes. Luckily, these changes are fairly simple to make by using the Alembic migrations
tool. Alembic compiles a list of SQL update statements based on the changes made to the model so that they do not have to
be written manually.

The following commands must be run each time the database model is updated:

    flask db migrate
    flask db upgrade
    
#### Running tests
It is also important to write unittests when developing the code base in order to prevent nasty gotcha's and minimise bugs.
This repo includes some neat examples of tests for this type of crud application, but they are mostly outdated and subject 
to fail. If you choose to update these tests for your application, then you will need to go through a set up process 
for the test database. This process is covered nicely in the original 
[scotch.io tutorial]( https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one), so please refer 
to the instructions outlined there.

#### Stopping the application
It is important to shutdown the database properly when you are finished with development. 

To shut down the PostgreSQL daemon process, run:

    pgctl -D PGDATA -l dreamteam_db_logfile.log stop
    
#### Useful tips for working with the database
The following tips might come in handy if you are new to PostgreSQL databases. There is a lot of conflicting information 
out there in the form of incomplete documentation, difference of opinion in forums, and subtle differences between databases
and ORMs. All database instructions listed in this README therefore do not necessarily represent the best or most efficient
ways of doing things, but will at least provide an easy entry into their set up and basic usage. It is my hope that this
may be useful for new users and save them from having to sift through the web of information out there and many hours of 
trial and error.

To start an existing database:

    pgctl -D [path to where the database files are stored] -l logfile.log start
    
To check if an instance of Postgres is running:
    
    ps  # should list a process called "postgres"
    
To start an interactive postgres shell and run commands against the db:

    psql [Name of the database]
    
Useful commands that can be run from within the interactive shell:

    \dl  # list the available databases
    \dt  # list the available database tables
    \du  # list the database roles
    \h  # help with SQL commands
    \q  # quit the interactive shell
    
Finally, a very useful open source Electron app for performing database queries using a GUI can be found here:
[sqlectron](https://sqlectron.github.io/).