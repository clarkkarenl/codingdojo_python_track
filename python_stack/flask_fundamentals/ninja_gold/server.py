# Assignment: Ninja Gold
# Karen Clark
# 2018-06-16

import datetime, random
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['balance'] = 0
    session['activities'] = ""
    return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('balance', None)
    session.pop('register', None)
    return redirect('/')

@app.route('/process_money', methods=['POST'])
def process_money():
    # TODO create a new function that does the heavy lifting for each target
    if request.method == 'POST':
        target = request.form['building']
        if target == 'farm':
            new_gold = random.randrange(10, 21)
            session['balance'] = int(session['balance']) + new_gold
            timestamp = datetime.datetime.now()
            session['activities'] = "Earned " + str(new_gold) + " gold from the farm! (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>" + session['activities']
        elif target == 'cave':
            new_gold = random.randrange(5, 11)
            session['balance'] = int(session['balance']) + new_gold
            timestamp = datetime.datetime.now()
            session['activities'] = "Earned " + str(new_gold) + " gold from the cave! (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>" + session['activities']
        elif target == 'house':
            new_gold = random.randrange(2, 6)
            session['balance'] = int(session['balance']) + new_gold
            timestamp = datetime.datetime.now()
            session['activities'] = "Earned " + str(new_gold) + " gold from the house! (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>" + session['activities']
        elif target == 'casino':
            new_gold = random.randrange(0, 51)
            timestamp = datetime.datetime.now()
            # If gold is not 0...
            if new_gold != 0:
                # ...determine if won or lost
                outcome = random.randrange(0,2)
                # lost gold
                if outcome == 1:
                    session['balance'] = int(session['balance']) - new_gold
                    session['activities'] = "Entered a casino and lost " + str(new_gold) + " gold...Ouch. (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>" + session['activities']
                    if session['balance'] <= 0:
                        session['balance'] = 50
                        session['activities'] = "You went bust! Thankfully, your rich uncle paid the debt and gave you 50 gold to keep going. (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>" + session['activities']
                # won gold
                else:
                    session['balance'] = int(session['balance']) + new_gold
                    session['activities'] = "Entered a casino and won " + str(new_gold) + " gold! (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>" + session['activities']
            # else new_gold was 0
            else:
                session['activities'] = "Entered a casino but did not win or lose gold. (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>" + session['activities']
        return render_template('index.html')
    
app.run(debug=True)
