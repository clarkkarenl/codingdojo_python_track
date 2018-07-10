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
    if 'comments' not in request.session:
        comments = ""
    return render(request, "survey/index.html")

def process(request):
    if request.method == 'POST':
        if 'name' not in request.session:
            name = request.session.get('name')
        if 'dojo_loc' not in request.session:
            dojo_loc = request.session.get('dojo_loc')
        if 'fav_lang' not in request.session:
            fav_lang = request.session.get('fav_lang')
        if 'comments' not in request.session:
            comments = request.session.get('comments')

        if not name or not dojo_loc or not fav_lang:
            messages.error(request, "Please provide values for all fields")
        
        return redirect("result.html")
        

def result(request):
    return redirect("/")
