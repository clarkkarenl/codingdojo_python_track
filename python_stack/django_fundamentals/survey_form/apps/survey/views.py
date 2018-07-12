# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render

# Create your views here.
def index(request):
    if 'name' not in request.session['data']['name']:
        request.session['data']['name'] = ""
    if 'dojo_loc' not in request.session['data']:
        request.session['data']['dojo_loc'] = ""
    if 'fav_lang' not in request.session['data']:
        request.session['data']['fav_lang'] = ""
    if 'comment_box' not in request.session['data']:
        request.session['data']['comment_box'] = ""
    return render(request, "survey/index.html")


def process(request):
    if request.method == 'POST':    
        name = request.POST['name']
        dojo_loc = request.POST['dojo_loc']
        fav_lang = request.POST['fav_lang']
        comment_box = request.POST['comment_box']

        request.session["data"]  = {
            "name" : name,
            "dojo_loc" : dojo_loc,
            "fav_lang" : fav_lang,
            "comment_box" : comment_box
        }

        return redirect("/survey/result")
 	 

def result(request):
    return render(request, "survey/result.html")
