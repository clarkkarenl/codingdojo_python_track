# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render
from time import gmtime, strftime

# Create your views here.
def index(request):
    # now = datetime.datetime.now()
    context = {
        "date_output": strftime("%b %d, %Y", gmtime()),
        "time_output": strftime("%H:%M %p", gmtime())
    }
    return render(request,'time_app/index.html', context)
