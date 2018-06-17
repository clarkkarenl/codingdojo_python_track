import datetime, os, random
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'fooBarBaz'

@app.route('/')
def index():
    return render_template('index.html')
        
@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        target = request.form.get('shop')
        if target == 'clothing':
            new_money = random.randrange(10, 21)
            session['balance'] = int(session['balance']) + new_money
            timestamp = datetime.datetime.now()
            session['register'] += "Received " + str(new_money) + " dollars from Clothing Store at " + timestamp.strftime("%Y/%m/%d %I:%M %p") + "<br/>"
        elif target == 'shoes':
            new_money = random.randrange(100, 141)
            session['balance'] = int(session['balance']) + new_money
            timestamp = datetime.datetime.now()
            session['register'] += "Received " + str(new_money) + " dollars from Shoe Store at " + timestamp.strftime("%Y/%m/%d %I:%M %p") + "<br/>"

        return render_template('index.html')
    
app.run(debug=True)