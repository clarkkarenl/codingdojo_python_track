# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    context = make_word(request)
    return render(request,'random_word_app/index.html', context)


def generate(request):
    context = make_word(request)
    return render(request,'random_word_app/index.html', context)


def reset(request):
    del request.session['counter']
    return redirect(index)


def make_word(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0

    request.session['counter'] += 1

    context = {
        "count_var" : request.session['counter'],
        "word" : get_random_string(14)
    }
    return context
