# Assignment: Registration Form
# Karen Clark
# 2018-06-17

# Assignment: Registration Form
# Create a simple registration page with fields and validations.
# When the form is submitted, make sure the user submits 
# appropriate information. If the user did not submit appropriate
# information, return the error(s) above the form that asks the 
# user to correct the information. 
# If the form with all the information is submitted properly, 
# simply have it say a message "Thanks for submitting your 
# information."
# Ninja Version:
# Add the validation that requires a password to have at least 
# 1 uppercase letter and 1 numeric value.
# Hacker Version:
# Add a birth-date field that must be validated as a valid date 
# and must be from the past.

from flask import Flask, render_template, request, redirect, session, flash
import datetime, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "ThisIsASecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        # handles missing value + format for email field
        if not EMAIL_REGEX.match(request.form['email']):
            flash("Please enter a valid email address")
        # handles missing value + contains no numbers for name fields
        elif not request.form['first_name'].isalpha():
            flash("First name cannot be blank and cannot contain numbers")
        elif not request.form['last_name'].isalpha():
            flash("Last name cannot be blank and cannot contain numbers")
        elif not request.form['birthdate']:
            flash("Please enter your birthdate")
        # handles birthdate in the future + proper date format
        elif request.form['birthdate'] > datetime.datetime.now().strftime("%Y-%m-%d"):
            flash("Please enter a birthdate in the past")
        # handles missing value + incorrect length for password field
        elif len(request.form['password']) < 8:
            flash("Password must be eight characters or longer")
        # password must have at least one number
        elif re.search('[0-9]',request.form['password']) is None:
            flash("Password must contain at least one number")
        # password must have at least one capital letter
        elif re.search('[A-Z]', request.form['password']) is None:
            flash("Password must contain at least one capital letter")
        # handles incorrect length + matching for confirmation field
        elif request.form['password'] != request.form['confirm_password']:
            flash("Password and confirmation password must match")
        else:
            result = request.form
            return render_template('success.html', result = result)
        # TODO preserve data so person doesn't lose it if a validation fails
        return redirect('/')
    elif request.method == 'GET':
        return render_template('success.html')

app.run(debug=True)