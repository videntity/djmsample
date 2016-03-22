from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

admin.site.site_header = 'Djmongo Administration'

urlpatterns = patterns('',
    url(r'^admin/',    include(admin.site.urls)),
    url(r'^',          include('djmongo.console.urls')),
    url(r'^console/',  include('djmongo.console.urls')),
    url(r'^search/',   include('djmongo.search.urls')),
    url(r'^import/',   include('djmongo.dataimport.urls')),
    url(r'^accounts/', include('djmongo.accounts.urls')),
    url(r'^write/',    include('djmongo.write.urls')),
    url(r'^aggregations/', include('djmongo.aggregations.urls')),
    
)
