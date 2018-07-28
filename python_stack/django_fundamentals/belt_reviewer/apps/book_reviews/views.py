# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import User, Book, Review


# a GET request to /
def index(request):
    return render(request, 'book_reviews/index.html')


# register for the site
def register(request):
    valid, result = User.objects.register_validator(request.POST)
    if not valid:
        for error in result:
            messages.error(request, error)
        return redirect('/')

    request.session['user_id'] = result.id
    request.session['logged_in'] = True
    return redirect('/books/')


# Login to the site once registered
def login(request):
    valid, result = User.objects.login_validator(request.POST)
    if not valid:
        for error in result:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['user_id'] = result.id
        request.session['logged_in'] = True
        return redirect('/books/')


# Users home page - books.html
def home(request):
    context = {
        'user' : request.session['user_id']
    }
    return render(request, 'book_reviews/books.html', context)


# GET request to /books/add 
def new(request):
    return render(request, 'book_reviews/add.html')


# POST to /books/create - calls the create method to 
# insert a new book and review into our database. 
def create(request):
    # valid, result = User.objects.user_create_validator(request.POST)
    # if not valid:
    #     for error in result:
    #         messages.error(request, error)
    #     return redirect('/users/new')
    # request.session['user_id'] = result.id
    return redirect('/books/' + str(result.id)+ '/')


# GET /books/<id> - calls the show method to display 
# the info for a particular book with given id.
def show(request, id):
    # context = {
    #     'user': User.objects.get(id=id)
    # }
    return render(request, 'book_reviews/detail.html', context)


# GET /books/destroy/<id>/ - calls the destroy method 
# to remove a particular book with the given id. 
def destroy(request, id):
    user_id = id
    User.objects.filter(id=user_id).delete()
    return redirect('/books/')
