# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render

# Create your views here.
def index(request):
    if 'name' not in request.session:
        name = ""
    if 'dojo_loc' not in request.session:
        dojo_loc = ""
    if 'fav_lang' not in request.session:
        fav_lang = ""
    if 'comment_box' not in request.session:
        comment_box = ""
    return render(request, "survey/index.html")


def process(request):
        "comment_box" : comment_box
    }

    if not name or not dojo_loc or not fav_lang:
        messages.error(request, "Please provide values for all fields")
    
    return redirect("survey/result", context)


def result(request):
    return render(request, "survey/result.html")
