# Assignment: Dojo Survey With Validation
# Karen Clark
# 2018-06-17

# Assignment: Dojo Survey With Validation
# Take the Dojo Survey assignment that you completed previously
# and add validations! The Name and Comment fields should be 
# validated so that they are not blank. Also, validate that the 
# comment field is no longer than 120 characters.

from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "ThisIsASecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        if len(request.form['name']) < 1:
            flash("Name cannot be empty")
            return redirect('/')
        elif len(request.form['comment']) < 1:
            flash("Comment cannot be empty")
            return redirect('/')
        elif len(request.form['name']) > 120:
            flash("Name cannot be longer than 120 characters")
            return redirect('/')
        elif len(request.form['comment']) > 120:
            flash("Comment cannot be longer than 120 characters")
            return redirect('/')
        else:
            result = request.form
            return render_template('result.html', result = result)
    elif request.method == 'GET':
        return render_template('result.html')

app.run(debug=True)
