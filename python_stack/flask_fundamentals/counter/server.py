# Assignment: Counter
# Karen Clark
# 2018-06-12
#
# Assignment: Counter
# Build a flask application that counts the number of times 
# the root route ('/') has been viewed. 
# Ninja Level 1
# Add a +2 button underneath the counter that reloads the 
# page and increments counter by 2. Add another route to 
# handle this functionality.
# Ninja Level 2
# Add a reset button that resets the counter back to 1. 
# Add another route to handle this functionality.

from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/', methods=['GET', 'POST'])
def index():
    session['counter'] = session['counter'] + 1
    return render_template('index.html')

# TODO: how can we clear these new routes from the URL so # the end user could reload the page?
@app.route('/plus_2', methods=['POST'])
def plus_2():
    session['counter'] = session['counter'] + 2
    return render_template('index.html')

@app.route('/clear_counter', methods=['POST'])
def clear_counter():
    session['counter'] = 0
    return render_template('index.html')

app.run(debug=True)