# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'courses/index.html')


def add_course(request):
    name = request.POST['course_name']
    desc = request.POST['desc']
    
    return redirect('index')

def destroy(request, id):
    
    return render(request, 'courses/delete.html')

