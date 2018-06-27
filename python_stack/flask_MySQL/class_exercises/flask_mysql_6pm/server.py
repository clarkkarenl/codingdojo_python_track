from flask import Flask, render_template, session, flash, request, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'users')

@app.route("/")
def index():
    users = mysql.query_db("SELECT * FROM users")
    return render_template("users.html", all_users=users)

@app.route("/add_users", methods=["POST"])
def add_users():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    password = request.form["password"]

    query = "INSERT INTO `users` (`first_name`, `last_name`, `email`, `password`, `created_at`, `updated_at`) VALUES (:field_one, :field_two, :field_three, :field_four, now(), now());"

    data = {
        "field_one": first_name,
        "field_two": last_name,
        "field_three": email,
        "field_four": password
    }

    result = mysql.query_db(query, data)
    return redirect("/")

@app.route("/users/<user_id>", methods = ["GET"])
def show(user_id):
    query = "SELECT * FROM users WHERE id = :specific_id"
    data = {
        "specific_id" : user_id
    }
    users = mysql.query_db(query, data)
    return render_template("show.html", users=users[0])

@app.route("/users/edit/<user_id>", methods = ["GET"])
def edit(user_id):
    query = "SELECT * FROM users WHERE id = :specific_id"
    data = {
        "specific_id" : user_id
    }
    users = mysql.query_db(query, data)
    return render_template("edit.html", users=users[0])

@app.route("/update_users/<user_id>", methods = ["POST"])
def update_users(user_id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    password = request.form["password"]

    query = "UPDATE users SET `first_name` = :field_one, `last_name` = :field_two, `email` = :field_three, `password`= :field_four, `updated_at` = now() WHERE id = :specific_id;"

    data = {
        "specific_id" : user_id,
        "field_one": first_name,
        "field_two": last_name,
        "field_three": email,
        "field_four": password
    }

    users = mysql.query_db(query, data)
    return redirect("/users/{}".format(user_id))

app.run(debug=True)