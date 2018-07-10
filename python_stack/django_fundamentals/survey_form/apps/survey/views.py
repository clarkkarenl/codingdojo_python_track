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
    if 'comment' not in request.session:
        comment = ""
    return render(request, "survey/index.html")


def process(request):
    if request.method == 'POST':
        request.session.name = request.POST['name']
        request.session.dojo_loc = request.POST['dojo_loc']
        request.session.fav_lang = request.POST['fav_lang']
        request.session.comment = request.POST['comment']

        return redirect("/survey/result", request=request)


def result(request):
    return render(request, "survey/result.html")
    
