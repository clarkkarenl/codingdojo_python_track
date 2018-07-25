# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render

from .models import User


def index(request):
    if 'new_user' not in request.session:
        request.session['new_user'] = ''
    if 'user_id' not in request.session:
        request.session['user_id'] = ''
    return render(request, 'loginreg/index.html')


def register(request):
    valid, result = User.objects.register_validator(request.POST)
    if not valid:
        for error in result:
            messages.error(request, error)
        return redirect('/')

    request.session['user_id'] = result.id
    request.session['new_user'] = True
    return redirect('/success')


def login(request):
    valid, result = User.objects.login_validator(request.POST)
    if not valid:
        for error in result:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['user_id'] = result.id
        request.session['new_user'] = False
        return redirect('/success')


def success(request):
    context = { 
        'user': User.objects.get(id=request.session['user_id']) 
    }

    return render(request, 'loginreg/success.html', context)
