# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render

# Create your views here.
def index(request):
    if 'word_list' not in request.session:
        request.session['word_list'] = []

    context = {
        "word_list": request.session['word_list']
    }

    return render(request, "words/index.html", context)

def add_word(request):
    if request.method == 'POST': 
        if 'word_list' not in request.session:
            request.session['word_list'] = []

        # Copy so we can modify the object
        temp_list = request.session['word_list']

        # Desired output format: 9:15:23pm, June 5th 2017
        ts = datetime.strftime(datetime.now(), "%I:%M:%S%p, %B %d %Y")

        # Make a dict for each entry in the list
        entry = {
            "word": request.POST['word'],
            "ts" : ts,
            "color" : request.POST['color'],
            "font" : request.POST['font']
        }

        temp_list.append(entry)
        request.session['word_list'] = temp_list
        request.session.modified = True

        return redirect("/")

def clear_session(request):
    if request.method == 'POST':
        session.clear()
    return redirect("/")