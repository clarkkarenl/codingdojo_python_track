from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.index),
    url(r'^word/$', views.index)
    # url(r'^random_word_app/generate/$', views.generate),
    # url(r'^random_word_app/reset/$', views.reset)
]