from flask import Flask, request, redirect, session, render_template, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'friends_app_db')
app.secret_key = "ThisIsASecret"

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)

@app.route('/add_friends', methods=['POST'])
def add_friend():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    occupation = request.form["occupation"]

    if len(request.form["first_name"]) > 1 and len(request.form["last_name"]) > 1 and len(request.form["occupation"]) > 1:
        query = "INSERT INTO `friends` (`first_name`, `last_name`, `occupation`, `created_at`, `updated_at`) VALUES (:field_one, :field_two, :field_three, now(), now());"
        data = {
            "field_one": first_name,
            "field_two": last_name,
            "field_three": occupation
        }
        result = mysql.query_db(query, data)
        return redirect("/")
    else:
        flash("Please input values into all fields.")
        return redirect("/")

app.run(debug=True)