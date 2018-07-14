# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    # Initialize purchases if not exists
    if 'purchases' not in request.session:
        request.session['purchases'] = []
    # Initialize totals if not exists
    print request.session
    if 'total_cost' not in request.session:
        request.session.total_cost = 0
    if 'total_items' not in request.session:
        request.session.total_items = 0
    if 'lifetime_spend' not in request.session:
        request.session.lifetime_spend = 0    

    context = {
        "purchases" : request.session['purchases'],
        "total_cost" : request.session.total_cost,
        "total_items" : request.session.total_items,
        "lifetime_spend":request.session.lifetime_spend
    }

    return render(request, "amadon/index.html", context)

def buy(request):
    if request.method == 'POST': 
        # Initialize purchases if not exists
        if 'purchases' not in request.session:
            request.session['purchases'] = []
        # Initialize totals if not exists
        if 'total_cost' not in request.session:
            request.session.total_cost = 0
        if 'total_items' not in request.session:
            request.session.total_items = 0
        if 'lifetime_spend' not in request.session:
            request.session.lifetime_spend = 0    

        ### PURCHASES ###
        # Handle this purchase. 
        # Make a copy of the list so we can modify
        temp_purchases = request.session['purchases']

        # First update purchases
        # change all existing "latest" flags to False
        for i in temp_purchases:
            if i["latest"] == True:
                i["latest"] = False

        # Desired output format: 9:15:23pm, June 5th 2017
        ts = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")

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

        # Make a dict for each entry in the list
        purchase = {
            "product_id": request.POST['product_id'],
            "unit_price": unit_price, 
            "ts" : ts,
            "quantity" : request.POST['quantity'],
            "latest" : True
        }

        temp_purchases.append(purchase)
        request.session['purchases'] = temp_purchases

        ### TOTALS ###
        # Handle the totals for this sale,
        # and for all time (for this session) 
        total_cost = unit_price * int(request.POST['quantity'])
        total_items = int(request.POST['quantity'])
        lifetime_spend = request.session.lifetime_spend + total_cost

        request.session.total_cost = total_cost
        print "Total cost:", total_cost
        request.session.total_items = total_items
        print "Total items:", total_items
        request.session.lifetime_spend = lifetime_spend
        print "Lifetime spend:", lifetime_spend

        context = {
            "purchases" : request.session['purchases'],
            "total_cost" : request.session.total_cost,
            "total_items" : request.session.total_items,
            "lifetime_spend":request.session.lifetime_spend
        }

        request.session.modified = True

    return redirect('/checkout')

def checkout(request):
    return render(request, "amadon/checkout.html", context)