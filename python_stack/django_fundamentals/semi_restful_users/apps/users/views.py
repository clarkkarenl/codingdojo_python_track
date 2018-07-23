# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import User

# Create your views here.
# a GET request to /users - calls the index method 
# to display all the users. This will need a template.
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'users/index.html', context)


# GET request to /users/new - calls the new method to 
# display a form allowing users to create a new user. 
# This will need a template.
def new(request):
    return render(request, 'users/new.html')


# POST to /users/create - calls the create method to 
# insert a new user record into our database. This POST 
# should be sent from the form on the page /users/new. 
# Have this redirect to /users/<id> once created.
def create(request):
    valid, result = User.objects.user_create_validator(request.POST)
    if not valid:
        for error in result:
            messages.error(request, error)
        return redirect('/users/new')
    request.session['user_id'] = result.id
    return redirect('/users/' + str(result.id)+ '/')


# GET request /users/<id>/edit - calls the edit method 
# to display a form allowing users to edit an existing 
# user with the given id. This will need a template
def edit(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'users/edit.html', context)


# GET /users/<id> - calls the show method to display 
# the info for a particular user with given id. This 
# will need a template.
def show(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'users/show.html', context)


# GET /users/<id>/destroy - calls the destroy method 
# to remove a particular user with the given id. Have 
# this redirect back to /users once deleted.
# TODO - this sucks but I can't quite get it right in models.py
# Fix this someday
def destroy(request, id):
    user_id = id
    User.objects.filter(id=user_id).delete()
    return redirect('/users/')


# POST /users/update - calls the update method to process 
# the submitted form sent from /users/<id>/edit. Have this 
# redirect to /users/<id> once updated.
def update(request, id):
    valid, result = User.objects.user_update_validator(request.POST)
    if not valid:
        for error in result:
            messages.error(request, error)
        return redirect('/users/' + id + '/edit/')
    else:
        return redirect('/users/' + id)
