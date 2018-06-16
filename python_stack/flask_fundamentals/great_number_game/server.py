# Assignment: Counter
# Karen Clark
# 2018-06-14
#
# Assignment: Great Number Game
# Create a site that when a user loads it creates a random number between
# 1-100 and stores the number in session. Allow the user to guess at the
# number and tell them when they are too high or too low. If they guess
# the correct number tell them and offer to play again.

import random
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

# load main page and draw a number if one doesn't exist
@app.route('/')
def main():
    session['draw'] = random.randrange(0, 101)
    session['counter'] = 1
    return render_template('index.html')

# client sends its guess using the input field
# TODO This doesn't actually work, but I need to move on
# will come back and finish this when I know more about routing!
@app.route('/guess', methods=['GET', 'POST'])
def guess_number():
    curr_guess = request.form.get('guess')
    session['counter'] = session['counter'] + 1
    # guess equals draw - win!
    if curr_guess == session['draw']:
        return render_template('index.html', status="match")
    # guess is less than draw
    elif curr_guess < session['draw']:
        return render_template('index.html', status="low")
    # guess is more than draw
    elif curr_guess > session['draw']:
        return render_template('index.html', status="high")
    else:
        return "ERROR: Please enter a number!"

# Clear the draw value and return to the starting page
@app.route('/play_again')
def play_again():
    session.pop('draw', None)
    return redirect('index.html')

app.run(debug=True)
