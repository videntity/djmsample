Djmongo Sample
==============


This is a Django project running the Djmongo application.

Here are some high-level configuration steps.


1. Clone the repo: `git clone https://github.com/videntity/djmsample.git`
2. Ensure MongoDB is installed and running.
3. Install the other requirements with pip `pip install -r djmsample/requirements.txt`
4. Setup the db. `python manage.py makemigrations`, `python manage.py migrate`.
5. Create a superuser. `python manage.py createsuperuser`.
6. Run the built in server:  `python manage.py runserver`  
7. Point to the URL: `http://127.0.0.1:8000/console`
