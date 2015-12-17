from django.conf.urls import patterns, include, url

from django.contrib import admin
from app1 import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cat/(?P<cat_id>[0-9]+)/$', views.cat, name='cat'),
    url(r'^cats/', views.cats, name='cats'),
    url(r'^cat/add/', views.add_cat, name='add Cat'),
    url(r'^login$', views.connexion, name='connexion'),
    url(r'^logout$', views.deconnexion, name='deconnexion'),
]
