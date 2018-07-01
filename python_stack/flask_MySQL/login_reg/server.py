from flask import Flask, request, redirect, session, render_template, flash
from mysqlconnection import MySQLConnector
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app,'login_reg')
app.secret_key = 'ThisIsASecret'
# Yes, this is dumb but we are meant to: 
# "Use md5 to hash passwords before inserting them into the database"
# And this is how we are expected to do that.
# If you know me, you know I'd NEVER use this in production!
salt = 'x0439175x'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def result():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    password = request.form["password"]
    confirm_pw = request.form["confirm_pw"]

    # Time to validate!
    # handles missing value + format for email field
    if not EMAIL_REGEX.match(request.form["email"]):
        flash('Please enter a valid email address')
        return redirect('/')
    # handles missing value + contains no numbers for name fields
    elif not request.form["first_name"] > 2 or not request.form["last_name"] > 2:
        flash('Name must be two characters or longer')
        return redirect('/')
    elif not request.form["first_name"].isalpha():
        flash('First name cannot be blank and cannot contain numbers')
        return redirect('/')
    elif not request.form["last_name"].isalpha():
        flash('Last name cannot be blank and cannot contain numbers')
        return redirect('/')
    # handles missing value + incorrect length for password
    elif len(request.form["password"]) < 8:
        flash('Password must be eight characters or longer')
        return redirect('/')
    # handles incorrect length + matching for confirmation field
    elif request.form["password"] != request.form["confirm_pw"]:
        flash('Password and confirmation password must match')
        return redirect('/')
    else:
        hashed_pw = md5.new(password + salt).hexdigest()

        query = 'INSERT INTO `users` (`first_name`, `last_name`, `email`, `password`, `created_at`, `updated_at`) VALUES (:field_one, :field_two, :field_three, :field_four, now(), now());'
        data = {
            'field_one': first_name,
            'field_two': last_name,
            'field_three': email,
            'field_four': hashed_pw
        }
        result = mysql.query_db(query, data)
        session["id"] = result
        return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    login_email = request.form["login_email"]
    login_pw = request.form["login_pw"]

    check_query = "SELECT * FROM users WHERE users.email = :login_email LIMIT 1"
    query_data = {'login_email': login_email}

    check_result = mysql.query_db(check_query, query_data) 
    encrypted_password = md5.new(login_pw + salt).hexdigest()

    if len(check_result) > 0:
        if check_result[0]['password'] == encrypted_password:
            # session["enc_pw"] = encrypted_password
            # session["db_pw"] = check_result[0]['password']
            session["id"] = check_result[0]['id']
            return render_template('login.html')
        else: 
            flash('Email address or password incorrect. Please try again')
            return redirect('/')
    else:
        flash('Email address or password incorrect. Please try again')
        return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    flash('You were logged out')
    return redirect('/')

app.run(debug=True)
