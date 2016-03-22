Djmongo Sample
==============


This is a full Django project designed to house the djmongo app.  Still a work in progress.

If you have access to this, you are likely committing to `django-djmongo` and/or `django-fhir`.

I recommend installing those from go locally in the apps folder using an `ln -s`.

I have a settings_local.py and a urls_local to help keep things separate for development.

I've posted them here:

settings_local.py


    from settings import *

    ROOT_URLCONF = 'djmsample.urls_local'

    INSTALLED_APPS += ('apps.fhir',)

urls_local.py


    from django.conf.urls import patterns, include, url
    from django.contrib import admin
    admin.autodiscover()

    admin.site.site_header = 'Djmongo Administration'

    urlpatterns = patterns('',
        url(r'^admin/',    include(admin.site.urls)),
        url(r'^',          include('apps.djmongo.console.urls')),
        url(r'^console/',  include('apps.djmongo.console.urls')),
        url(r'^search/',   include('apps.djmongo.search.urls')),
        url(r'^import/',   include('apps.djmongo.dataimport.urls')),
        url(r'^write/',    include('apps.djmongo.write.urls')),
        url(r'^accounts/', include('apps.djmongo.accounts.urls')),
        url(r'^aggregations/', include('apps.djmongo.aggregations.urls')),
        url(r'^fhir/',     include('apps.fhir.urls')),
    )