# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.shortcuts import render, redirect


def index(request):
    # Initialize purchases if not exists
    if 'purchases' not in request.session:
        request.session['purchases'] = []
    # Initialize tally if not exists
    if 'tally' not in request.session:
        request.session['tally'] = {
            'total_cost' : 0,
            'lifetime_items' : 0,
            'lifetime_spend' : 0
        }

    return render(request, "amadon/index.html")


def buy(request):
    if request.method == 'POST': 
        # Initialize purchases if not exists
        if 'purchases' not in request.session:
            request.session['purchases'] = []
        # Initialize totals if not exists
        if 'tally' not in request.session:
            request.session['tally'] = {
                'total_cost' : 0,
                'lifetime_items' : 0,
                'lifetime_spend' : 0
            }
   
        ### PURCHASES ###
        # Update purchases, change all "latest" flags to False
        for i in request.session['purchases']:
            if i["latest"] == True:
                i["latest"] = False

        # Presumably in future assignments we'll look
        # these up in a database...? :P
            # T-shirt = 1015 = $19.99
            # Sweater = 1016 = $29.99
            # Cup = 1017 = $4.99
            # Book = 1018 = $49.99
        product_map = {
            '1015': 19.99,
            '1016': 29.99,
            '1017': 4.99,
            '1018': 49.99
        }
        unit_price = product_map[request.POST['product_id']]

        # Capture the timestamp
        # Desired output format: 2017-06-01T06:15:49
        ts = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")

        # Make a dict for each entry in the list
        new_purchase = {
            "product_id": request.POST['product_id'],
            "unit_price": unit_price, 
            "ts" : ts,
            "quantity" : int(request.POST['quantity']),
            "latest" : True
        }

        request.session['purchases'].append(new_purchase)
        request.session.modified = True

        ### TALLY ###
        # Handle the totals for this sale,
        # and for all time (for this session)
        request.session['tally']['lifetime_items'] += int(request.POST['quantity'])
        request.session['tally']['total_cost'] = unit_price * float(int(request.POST['quantity']))
        request.session['tally']['lifetime_spend'] += unit_price * float(int(request.POST['quantity']))

        request.session.modified = True
        return redirect('/checkout')


def checkout(request):
    return render(request, "amadon/checkout.html")