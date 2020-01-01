Djmongo Sample
==============

This is a Django project running the Djmongo API Builder.  It is based on Python 3.6 and Django 2.2.


Quick Start
-----------


1. Clone this repository: `git clone https://github.com/videntity/djmsample.git`
2. Ensure MongoDB is installed and running.
3.  Adjust the value of `MONGODB_CLIENT` environment variable if necessary. The default value is `mongodb://localhost:27017/`. On Linux for example `export MONGODB_CLIENT=mongodb://example.com:27017/`. 
4. While not absolutely required, its a good idea to create a Python virtualenv. For example `mkvirtualenv djmsample -p python3`.
3. Install the Python requirements with pip. `pip install -r requirements.txt`
4. Setup the relational database. `python manage.py migrate`.  (Note the relational database holds configuration data for each API you create.)
5. Create a superuser so you can login to the API console. `python manage.py createsuperuser`.
6. Run the built in server:  `python manage.py runserver`  
7. Point your web browser to the URL: `http://127.0.0.1:8000/`
8. Login and start building your API gateway!

Please check out our open source command line tools for importing data into
MongoDB at https://github.com/videntity/json-data-tools

