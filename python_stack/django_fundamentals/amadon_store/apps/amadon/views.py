# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.shortcuts import render, redirect


def index(request):
    # Initialize purchases if not exists
    if 'purchases' not in request.session:
        request.session['purchases'] = []
    # Initialize totals if not exists
    if 'tally' not in request.session:
        request.session['tally'] = []

    return render(request, "amadon/index.html")


def buy(request):
    if request.method == 'POST': 
        # Initialize purchases if not exists
        if 'purchases' not in request.session:
            request.session['purchases'] = []
        # Initialize totals if not exists
        if 'tally' not in request.session:
            request.session['tally'] = []
   
        product_id = request.POST['product_id']
        quantity = int(request.POST['quantity'])

        ### PURCHASES ###
        # Handle this purchase. 
        # Make a copy of the list so we can modify
        temp_purchases = request.session['purchases']

        # Update purchases, change all "latest" flags to False
        for i in temp_purchases:
            if i["latest"] == True:
                i["latest"] = False

        # Presumably in future assignments we'll look
        # these up in a database...? :P
            # T-shirt = 1015 = $19.99
            # Sweater = 1016 = $29.99
            # Cup = 1017 = $4.99
            # Book = 1018 = $49.99
        if request.POST['product_id'] == '1015':
            unit_price = 19.99
        elif request.POST['product_id'] == '1016':
            unit_price = 29.99
        elif request.POST['product_id'] == '1017':
            unit_price = 4.99
        elif request.POST['product_id'] == '1018':
            unit_price = 49.99

        # Capture the timestamp
        # Desired output format: 2017-06-01T06:15:49
        ts = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")

        # Make a dict for each entry in the list
        new_purchase = {
            "product_id": product_id,
            "unit_price": unit_price, 
            "ts" : ts,
            "quantity" : quantity,
            "latest" : True
        }
        temp_purchases.append(new_purchase)
        request.session['purchases'] = temp_purchases

        ### TALLY ###
        # Handle the totals for this sale,
        # and for all time (for this session)
        temp_tally = request.session['tally']
        request.session['tally'] = []

        new_tally = {
            "total_cost": unit_price * quantity,
            "total_items": temp_tally.total_items + quantity,
            "lifetime_spend": temp_tally.lifetime_spend + total_cost
        }

        request.session['tally'] = temp_tally
        request.session.modified = True

        return redirect('/checkout')


def checkout(request):
    return render(request, "amadon/checkout.html")