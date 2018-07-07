# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# # Create your views here.
# def index(request):
#     print request
#     return render(request, 'dash/index.html')

def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "dash/index.html", context)