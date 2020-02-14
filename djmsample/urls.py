from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
admin.autodiscover()

admin.site.site_header = 'Djmongo Administration'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^djm/', include('djmongo.urls')),
    url(r'^$', TemplateView.as_view(template_name='djmongo/console/splash.html'),
        name='djmongo_splash'),
    # url(r'^console/', include('djmongo.console.urls')),
    # url(r'^search/', include('djmongo.search.urls')),
    # url(r'^import/', include('djmongo.dataimport.urls')),
    # url(r'^accounts/', include('djmongo.accounts.urls')),
    # url(r'^write/', include('djmongo.write.urls')),
    # url(r'^aggregations/', include('djmongo.aggregations.urls')),

]
