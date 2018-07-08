# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    count_var = request.session.get('counter', 1)

    context = {
        "count_var" : int(count_var),
        "word" : get_random_string(14)
    }
    return render(request,'random_word_app/index.html', context)

def generate(request):
    # num_visits=request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits+1
    # 'num_visits':num_visits
    count_var = request.session['counter']
    request.session['counter'] = count_var + 1

    context = {
        "count_var" : count_var,
        "word" : get_random_string(14)
    }
    return render(request,'random_word_app/index.html', context)

def reset(request):
    del request.session['counter']
    return redirect(index)
