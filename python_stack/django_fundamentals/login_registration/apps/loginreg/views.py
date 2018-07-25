# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import User

# Create your views here.
def index(request):
    return render(request, 'loginreg/index.html')

def register(request):
    # take the values and ask for them to be validated
    # send errors if failed
    # send to new page if succeeded
    # TODO: need a session value to indicate if has previously 
    # logged in or ... something. So we can toggle message
    # based on register or log in action.
    return redirect('success')


def success(request):
    context = {}
    return render(request, 'loginreg/success.html', context)