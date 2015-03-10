from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.sites.models import Site

from home import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fotoweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'home.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)

admin.site.unregister(Site);
