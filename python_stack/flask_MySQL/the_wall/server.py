from flask import Flask, request, redirect, session, render_template, flash
from mysqlconnection import MySQLConnector
from time import time
import md5, re, pytz

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
        msg_query = "SELECT CONCAT(`users`.`first_name`,\" \", `users`.`last_name`) as `user_name`, `users`.`id` as `user_id`, DATE_FORMAT(`messages`.`created_at`, \"%h:%i%p %M %D, %Y\") as `created_at` , `messages`.`id` as `message_id`, `messages`.`message` as `message` FROM `messages` JOIN `users` ON `users`.`id` = `messages`.`user_id` ORDER BY `messages`.`created_at` DESC;"

        msg_list = mysql.query_db(msg_query)

        msg_data = list()
        for m in msg_list:
            msg_data.append(str(m['message_id']))

        msg_data = msg_data[:-1]

        comment_query = "SELECT `messages`.`id` as `message_id`, `comments`.`id` as `comment_id`, CONCAT(`users`.`first_name`,\" \", `users`.`last_name`) as `user_name`, `comments`.`comment` as `comment`, DATE_FORMAT(`comments`.`created_at`, \"%h:%i%p %M %D, %Y\") as `created_at` FROM `messages` JOIN `comments` ON `messages`.`id` = `comments`.`message_id` LEFT JOIN `users` ON `comments`.`user_id` = `users`.`id` WHERE  `messages`.`id` IN :field_one ORDER BY `comments`.`created_at` ASC;"

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

@app.route('/delete_own_msg', methods=['POST'])
def delete_own_msg():
    #
    # Delete own messages for Extra Credit I (optional)
    #
    # TODO: implement logging so we can audit events later
    if session["id"]:
        msg_to_delete = request.form['msg_id']
        requester_user_id = request.form['user_id']

        # Get the user ID of the person who posted the message
        msg_user_id_query = "SELECT `messages`.`user_id` FROM `messages` WHERE `messages`.`id` = :field_one;"
        msg_user_id_data = { 'field_one' : msg_to_delete }
        msg_user_id_result = mysql.query_db(msg_user_id_query, msg_user_id_data)

        # TODO: Grey out the button if not message's poster
        # but for now.... logic on the server side... *sigh*
        if int(requester_user_id) - int(str(msg_user_id_result[0]['user_id'])) > 0:
            flash('You can only delete your own messages')
            return redirect('/get_msgs')

        # 
        # Delete own msg only if posted < 30 mins for Extra Credit II (optional)
        #
        # Let's see when the message in the delete request was posted
        msg_date_query = "SELECT unix_timestamp(`messages`.`created_at`) as `created_at`  FROM `messages` WHERE `messages`.`id` = :field_one;"
        msg_date_data = { 'field_one' : msg_to_delete }
        msg_date_result = mysql.query_db(msg_date_query, msg_date_data)

        # This section is a cop-out because the DB is Pacific Time
        # and me, the user, is on Pacific Time.
        # TODO: Make this work as UTC / offset with agent string
        if int(time()) - int(str(msg_date_result[0]['created_at'])) > 1800:
            flash('Sorry, you can only delete messages you created in the last 30 minutes')
            return redirect('/get_msgs')

        # Comments deletion query
        delete_comment_query = "DELETE FROM `comments` WHERE `comments`.`message_id` = :field_one;"
        delete_comment_data = { 'field_one' : msg_to_delete }

        # Messages delete query
        delete_msg_query = "DELETE FROM `messages` WHERE `messages`.`id` = :field_one AND `messages`.`user_id` = :field_two;"
        delete_msg_data = {
            'field_one' : msg_to_delete,
            'field_two' : requester_user_id
        }

        try:
            # First delete comments for that message bc CONSTRAINT FK
            comment_delete = mysql.query_db(delete_comment_query, delete_comment_data)

            # Then, delete messages
            msg_delete = mysql.query_db(delete_msg_query, delete_msg_data)
            flash('Deleted comments and messages')
            return redirect('/get_msgs')
        except Exception as e:
            flash("Nope, sorry! Error: " + str(e))
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

        register_user_query = 'INSERT INTO `users` (`first_name`, `last_name`, `email`, `password`, `created_at`, `updated_at`) VALUES (:field_one, :field_two, :field_three, :field_four, now(), now());'
        register_user_data = {
            'field_one': first_name,
            'field_two': last_name,
            'field_three': email,
            'field_four': hashed_pw
        }
        register_user_result = mysql.query_db(register_user_query, register_user_data)
        session["id"] = register_user_result
        flash("Thank you for registering! Please log in to access The Wall!")
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    login_email = request.form["login_email"]
    login_pw = request.form["login_pw"]

    login_check_query = "SELECT * FROM users WHERE users.email = :login_email LIMIT 1"
    login_query_data = {'login_email': login_email}

    login_check_result = mysql.query_db(login_check_query, login_query_data) 
    encrypted_password = md5.new(login_pw + salt).hexdigest()

    if len(login_check_result) > 0:
        if login_check_result[0]['password'] == encrypted_password:
            session["name"] = login_check_result[0]['first_name']
            session["id"] = login_check_result[0]['id']
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
