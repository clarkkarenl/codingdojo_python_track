# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render

# Create your views here.
def index(request):
    return render(request, "words/index.html")

def process(request):
    pass