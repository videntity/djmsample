Djmongo Sample
==============


This is a Django project running the [Djmongo](https://github.com/videntity/django-djmongo) application.

Here are the basic configuration steps.


1. Clone the repo: `git clone https://github.com/videntity/djmsample.git`, and cd into repo: `cd djmsample`
2. Ensure [MongoDB](https://docs.mongodb.com/manual/installation/) is installed and running.
3. Install the other requirements with pip `pip install -r djmsample/requirements.txt`
4. Setup the db. `python manage.py makemigrations`, `python manage.py migrate`.
5. Create a superuser. `python manage.py createsuperuser`.
6. Run the built in server:  `python manage.py runserver`  
7. Point to the URL: `http://127.0.0.1:8000/djm/console/`
8. Login and start building your API gateway.

Please check out our open source command line tools for importing data into MongoDB at https://github.com/videntity/json-data-tools


