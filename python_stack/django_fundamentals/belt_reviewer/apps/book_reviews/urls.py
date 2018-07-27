from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^books/$', views.home),
    url(r'^books/add/$', views.new),
    url(r'^books/create/$', views.create),
    url(r'^books/(?P<id>\d+)/$', views.show),
    url(r'^books/destroy/(?P<id>\d+)/$', views.destroy),
]
