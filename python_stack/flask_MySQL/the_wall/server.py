from flask import Flask, request, redirect, session, render_template, flash
from mysqlconnection import MySQLConnector
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app,'the_wall')

app.secret_key = 'AnotherBrickIn'
# Yes, this is dumb but we are meant to: 
# "Use md5 to hash passwords before inserting them into the database"
# And this is how we are expected to do that.
# If you know me, you know I'd NEVER use this in production!
salt = '0x5d1919'

@app.route('/', methods=['GET'])
def index(): 
    return render_template('index.html')

@app.route('/get_msgs', methods=['GET'])
def get_msgs():    
    if session["id"]:
        msg_query = "SELECT CONCAT(`users`.`first_name`,\" \", `users`.`last_name`) as `user_name`, DATE_FORMAT(`messages`.`created_at`, \"%M %d %Y\") as `created_at` , `messages`.`id` as `message_id`, `messages`.`message` as `message` FROM `messages` JOIN `users` ON `users`.`id` = `messages`.`user_id` WHERE `messages`.`user_id` = :field_one ORDER BY `messages`.`created_at` DESC;"
        user_data = { 'field_one': session["id"]}
        msg_list = mysql.query_db(msg_query, user_data)
        msg_data = ''

        for m in msg_list:
            msg_data += (str(m['message_id']) + ',')

        msg_data = msg_data[:-1]

        comment_query = "SELECT `messages`.`id` as `message_id`, `comments`.`id` as `comment_id`, `comments`.`comment` as `comment`, DATE_FORMAT(`comments`.`created_at`, \"%M %d %Y\") as `created_at` FROM `messages` JOIN `comments` ON `messages`.`id` = `comments`.`message_id` WHERE  `messages`.`id` IN (:field_one) ORDER BY `comments`.`created_at` ASC;"
        comment_data = { 'field_one': msg_data }
        comment_list = mysql.query_db(comment_query, comment_data)

        return render_template('wall.html', msg_list = msg_list, comment_list = comment_list)
    else:
        flash("You are not logged in")
        return render_template('index.html')

@app.route('/post_msg', methods=['POST'])
def post_msg():
    if session["id"]:
        new_msg = request.form['msg']
        # Don't do anything if the message is empty
        if len(new_msg) == 0:
            return redirect('/get_msgs')
        else:
            new_msg_query = "INSERT INTO `messages`(`user_id`, `message`, `created_at`, `updated_at`) VALUES (:field_one, :field_two, now(), now());"
            new_msg_data = {
                'field_one' : session['id'],
                'field_two' : new_msg
            }
            # TODO Include any comments for each message
            msg_added = mysql.query_db(new_msg_query, new_msg_data)
            return redirect('/get_msgs')
    else:
        flash("You are not logged in")
        return redirect('/')

@app.route('/post_comment', methods=['POST'])
def post_msg_comment():
    if session["id"]:
        new_comment = request.form['msg_comment']
        msg_id = request.form['msg_id']
        if len(new_comment) == 0:
            return redirect('/get_msgs')
        else:
            new_comment_query = "INSERT INTO `comments`(`message_id`,  `user_id`, `comment`, `created_at`, `updated_at`) VALUES (:field_one, :field_two, :field_three, now(), now());"
            new_comment_data = {
                'field_one' : msg_id,
                'field_two' : session['id'], 
                'field_three' : new_comment
            }
            comment_added = mysql.query_db(new_comment_query, new_comment_data)
            return redirect('/get_msgs')
    else:
        flash("You are not logged in")
        return redirect('/')


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
        flash("Thank you for registering! Please log in to access The Wall!")
        return redirect('/')

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
            session["name"] = check_result[0]['first_name']
            session["id"] = check_result[0]['id']
            # TODO Is this right?
            return redirect('get_msgs')
        else: 
            flash('Email address or password incorrect. Please try again')
            return redirect('/')
    else:
        flash('Email address or password incorrect. Please try again')
        return redirect('/')

@app.route('/logout_page')
def logout_page():
    return render_template('logout.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You were logged out')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
