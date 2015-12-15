from django.conf.urls import patterns, include, url

from django.contrib import admin
from app1 import views

admin.autodiscover()

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.home),
    url(r'^admin/', include(admin.site.urls)),
    # ex: /polls/5/
    url(r'^(?P<cat_id>[0-9]+)/$', views.cat, name='cat'),
    # ex: /polls/5/results/
    url(r'^cats/', views.cats, name='cats'),
]
