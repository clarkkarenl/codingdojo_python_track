# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse


# /blogs - display "placeholder to later display all the 
# list of blogs" via HttpResponse. Have this be handled by 
# a method named 'index'.
def index(request):
    response = 'placeholder to later display all the list of blogs'
    return HttpResponse(response)


# /blogs/new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'.
def new(request):
    response = 'placeholder to display a new form to create a new blog'
    return HttpResponse(response)


# /blogs/create - Have this be handled by a method named 'create'.  For now, have this url redirect to /blogs.
def create(request):
    return redirect('/blogs')


# /blogs/{{number}} - display 'placeholder to display blog {{number}}.  For example /blogs/15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'.
def show(request, number):
    response = "placeholder to display blog %s" % (number)
    return HttpResponse(response)


# /blogs/{{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'.
def edit(request, number):
    response = "placeholder to edit blog %s" % (number)
    return HttpResponse(response)

# /blogs/{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /blogs. 
def destroy(request, number):
    return redirect('/blogs')