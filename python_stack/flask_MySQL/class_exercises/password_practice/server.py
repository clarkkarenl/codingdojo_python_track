from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import md5
import os, binascii

app = Flask(__name__)
mysql = MySQLConnector(app,'users')

@app.route('/users/create', methods=['POST'])
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email'] # will be used as for login
    password = request.form['password']

    salt =  binascii.b2a_hex(os.urandom(15))
    hashed_pw = md5.new(password + salt).hexdigest()

    insert_query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :hashed_pw, :salt, NOW(), NOW());"
    
    query_data = { 
        'first_name': first_name,
        'last_name' : last_name,
        'email': email,
        'hashed_pw': hashed_pw,
        'salt': salt
    }

    mysql.query_db(insert_query, query_data)

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"

    query_data = {'email': email}

    user = mysql.query_db(user_query, query_data)

    if len(user) != 0:
        encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
    if user[0]['password'] == encrypted_password:
    # this means we have a successful login!
    else:
        # invalid password!
    else:
    # invalid email!

app.run(debug=True)