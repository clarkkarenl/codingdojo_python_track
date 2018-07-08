# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    # if it's the users first visit, won't have this var,
    # so set it
    if 'counter' not in request.session:
        request.session['counter'] = 1

    count_var = request.session['counter']

    context = {
        "count_var" : count_var,
        "word" : get_random_string(14)
    }
    return render(request,'random_word_app/index.html', context)

def generate(request):
    count_var = request.session.get('counter')
    count_var += 1
    request.session['counter'] += 1

    context = {
        "count_var" : count_var,
        "word" : get_random_string(14)
    }
    return render(request,'random_word_app/index.html', context)

def reset(request):
    del request.session['counter']
    return redirect(index)
