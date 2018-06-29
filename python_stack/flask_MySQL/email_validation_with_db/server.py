from flask import Flask, request, redirect, session, render_template, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app,'email_validation')
app.secret_key = "ThisIsASecret"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    email = request.form["email"]

    if len(request.form['email']) < 1 or not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid!")
        return redirect('/')
    else:
        query = "INSERT INTO `emails` (`email`, `created_at`, `updated_at`) VALUES (:field_one, now(), now());"
        data = {"field_one": email}
        result = mysql.query_db(query, data)


    emails_query = "SELECT email, created_at FROM emails ORDER BY created_at DESC"
    emails = mysql.query_db(emails_query)

    return render_template("success.html", all_emails=emails, email=email)

app.run(debug=True)


        