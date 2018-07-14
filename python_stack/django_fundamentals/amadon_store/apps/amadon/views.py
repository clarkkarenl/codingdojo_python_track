# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "amadon/index.html")


def checkout(request):
    # T-shirt = 1015 = $19.99
    # Sweater = 1016 = $29.99
    # Cup = 1017 = $4.99
    # Book = 1018 = $49.99
    return render(request, "amadon/checkout.html")