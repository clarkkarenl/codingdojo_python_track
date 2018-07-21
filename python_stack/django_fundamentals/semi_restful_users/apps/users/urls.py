from django.conf.urls import url

from . import views, models

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$', views.new),
    url(r'^create/$', views.create),
    url(r'^(?P<id>\d+)$', views.show),
    url(r'^(?P<id>\d+)/edit/$', views.edit),
    url(r'^(?P<id>\d+)/delete/$', views.destroy),
    url(r'^update/$', views.update)
]
