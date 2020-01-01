Djmongo Sample
==============


This is a Django project running the Djmongo API Builder.

Quick Start
-----------


1. Clone this repository: `git clone https://github.com/videntity/djmsample.git`
2. Ensure MongoDB is installed and running. MONGODB_CLIENT default value is `mongodb://localhost:27017/`. Adjust this if needed.
by setting an the environment variable. On Linux for example `export MONGODB_CLIENT=mongodb://example.com:27017/`. 
3. Install the other requirements with pip `pip install -r requirements.txt`
4. Setup the db. `python manage.py migrate`.
5. Create a superuser. `python manage.py createsuperuser`.
6. Run the built in server:  `python manage.py runserver`  
7. Point your web browser to the URL: `http://127.0.0.1:8000/`
8. Login and start building your API gateway!

Please check out our open source command line tools for importing data into
MongoDB at https://github.com/videntity/json-data-tools


