# Assignment: Counter
# Karen Clark
# 2018-06-16
#
# Assignment: Ninja Game
# Create a site that when a user loads it creates a random number between
# 1-100 and stores the number in session. Allow the user to guess at the
# number and tell them when they are too high or too low. If they guess
# the correct number tell them and offer to play again.

import datetime
import random
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')
        
@app.route('/process', methods=['GET', 'POST'])
def process():
    # TODO create a new function that does the heavy lifting for each target
    if request.method == 'POST':
        target = request.form.get('shop')
        if target == 'farm':
            new_gold = random.randrange(10, 21)
            session['balance'] = int(session['balance']) + new_gold
            timestamp = datetime.datetime.now()
            session['register'] += "Earned " + str(new_gold) + " gold from the farm! (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>"
        elif target == 'cave':
            new_gold = random.randrange(5, 11)
            session['balance'] = int(session['balance']) + new_gold
            timestamp = datetime.datetime.now()
            session['register'] += "Earned " + str(new_gold) + " gold from the cave! (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>"
        elif target == 'house':
            new_gold = random.randrange(5, 11)
            session['balance'] = int(session['balance']) + new_gold
            timestamp = datetime.datetime.now()
            session['register'] += "Earned " + str(new_gold) + " gold from the house! (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>"
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
                    session['register'] += "Entered a casino and lost " + str(new_gold) + " gold...Ouch. (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>"
                # won gold
                else:
                    session['balance'] = int(session['balance']) + new_gold
                    session['register'] += "Entered a casino and won " + str(new_gold) + " gold! (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>"
            # else new_gold was 0
            else:
                session['register'] += "Entered a casino but did not win or lose gold. (" + timestamp.strftime("%Y/%m/%d %I:%M %p") + ")<br/>"
        return render_template('index.html')
    
app.run(debug=True)
