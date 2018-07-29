# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import User, Book, Review

####### INDEX PAGE #######
# a GET request to /
def index(request):
    if 'logged_in' not in request.session:
        request.session['logged_in'] = ''
    if 'user_id' not in request.session:
        request.session['user_id'] = ''
    return render(request, 'book_reviews/index.html')
##########################################


####### REG / LOGIN / LOGOUT #######
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
    print request.session['user_id']
    print request.session['logged_in']

    valid, result = User.objects.login_validator(request.POST)
    if not valid:
        for error in result:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['user_id'] = result.id
        request.session['logged_in'] = True
        return redirect('/books/')


def logout(request):
    print request.session['user_id']
    print request.session['logged_in']
    request.session.clear()
    return redirect('/')
##########################################


####### BOOK STUFF #######
# Users home page - books.html
def home(request):
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'books' : Book.objects.all(),
        'reviews': Review.objects.all()
    }
    return render(request, 'book_reviews/books.html', context)


# GET request to /books/add 
def new(request):
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'author_set' : Book.objects.values_list('author', flat=True).distinct().order_by('author')
    }
    return render(request, 'book_reviews/add.html', context)


# POST to /books/create - calls the create method to 
# insert a new book and review into our database. 
def create(request):
    user_id = request.session['user_id']
    valid, result = Book.objects.book_create_validator(request.POST, user_id)

    if not valid:
        for error in result:
            messages.error(request, error)
        return redirect('/books/add/')

    return redirect('/books/' + str(result.id)+ '/')


# POST to /books/create_review - calls the create method
# to insert a review into our database. 
def create_review(request):
    # user_id = request.session['user_id']
    valid, result = Review.objects.review_create_validator(request.POST)

    if not valid:
        for error in result:
            messages.error(request, error)
        return redirect('/books/')

    return redirect('/books/' + result + '/')

# GET /books/<id> - calls the show method to display 
# the info for a particular book with given id.
def show(request, id):
    context = {
        'book': Book.objects.get(id=id),
        'reviews': Review.objects.filter(book=id),
        'user' : User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'book_reviews/detail.html', context)


# GET /books/destroy/<id>/ - calls the destroy method 
# to remove a particular book with the given id. 
def destroy(request, id):
    user_id = id
    User.objects.filter(id=user_id).delete()
    return redirect('/books/')
##########################################


####### USER STUFF #######
def user_page(request, id):
    user_id = id
    context = {
        'user' : User.objects.get(id=user_id),
        'my_reviews': Review.objects.filter(user=user_id),
        'num_reviews': Review.objects.filter(user=user_id).count()
    }
    return render(request, 'book_reviews/users.html', context)
##########################################