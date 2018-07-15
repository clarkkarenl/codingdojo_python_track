# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime, random
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'balance' not in request.session:
        request.session['balance'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, "ninja_gold/index.html")

def process_money(request):
    if request.method == 'POST':
        target = request.POST['building']

        new_gold_map = {
            'farm': random.randrange(10, 21),
            'cave': random.randrange(5, 11),
            'house': random.randrange(2, 6),
            'casino': random.randrange(0, 51)
        }

        new_gold = new_gold_map[target]
        timestamp = datetime.datetime.now()

        if target == 'farm' or target == 'cave' or target == 'house':
            request.session['balance'] = int(request.session['balance']) + new_gold
            request.session['activities'].append("Earned " + str(new_gold) + " gold from the "+ target +"! (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>")
        elif target == 'casino':
            # If gold is not 0...
            if new_gold != 0:
                # ...determine if won or lost
                outcome = random.randrange(0,2)
                # lost gold
                if outcome == 1:
                    request.session['balance'] = int(request.session['balance']) - new_gold
                    request.session['activities'].append("Entered a casino and lost " + str(new_gold) + " gold...Ouch. (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>")
                    if request.session['balance'] <= 0:
                        request.session['balance'] = 50
                        request.session['activities'].append("You went bust! Thankfully, your rich uncle paid the debt and gave you 50 gold to keep going. (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>")
                # won gold
                else:
                    request.session['balance'] = int(request.session['balance']) + new_gold
                    request.session['activities'].append("Entered a casino and won " + str(new_gold) + " gold! (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>")
            # else new_gold was 0
            else:
                request.session['activities'].append("Entered a casino but did not win or lose gold. (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>")
        return redirect('/')


def reset(request):
    if request.method == 'POST':
        request.session.clear()
        return redirect('/')
