from django.conf.urls import patterns, include, url

from django.contrib import admin
from app1 import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^hello/$', views.hello),
)
