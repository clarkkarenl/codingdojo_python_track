# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import Course


# Index page contains form to add a course, and a
# table of current courses & links to remove each
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)


# Add course is a method to handle the request from
# the form on the index page
def add_course(request):
    valid, result = Course.objects.validator(request.POST)
    if not valid:
        for error in result:
            messages.error(request, error)

    return redirect('/')


# destroy is the URL that leads to the delete page
def destroy(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'courses/delete.html', context)


# delete is the operation that removes the value from the db
def delete(request, id):
    course_id = id
    Course.objects.filter(id=course_id).delete()
    return redirect('/')