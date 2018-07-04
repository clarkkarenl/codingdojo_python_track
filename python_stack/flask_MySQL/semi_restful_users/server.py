from flask import Flask, request, redirect, session, render_template, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'friends')
app.secret_key = 'SekritzRSekrit'

# GET request to /users - calls the index method to display all the users.
@app.route('/users', methods=['GET'])
def index(): 
    get_users_query = "SELECT `users`.`id` as `user_id`, CONCAT(`users`.`first_name`,\" \", `users`.`last_name`) as `user_name`,  `users`.`email` as `email`, DATE_FORMAT(`users`.`created_at`, \"%M %D, %Y\") as `created_at` FROM `users` ORDER BY `users`.`created_at` ASC;"
    user_list = mysql.query_db(get_users_query)
    return render_template('users.html', users = user_list)


# GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an existing user with the given id. 
@app.route('/users/<id>/edit', methods=['GET'])
def edit(id):
    
    get_edit_user_query = "SELECT `users`.`id` as `user_id`,`users`.`first_name` as `first_name`, `users`.`last_name` as `last_name`, `users`.`email` as `email` FROM `users` WHERE `users`.`id` = :field_one;"

    get_edit_user_data = {'field_one' : id}

    user_to_edit = mysql.query_db(get_edit_user_query, get_edit_user_data)
    return render_template('edit.html', user=user_to_edit[0])


# POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit. Have this redirect to /users/<id> once updated.


# GET /users/<id> - calls the show method to display the info for a particular user with given id.
@app.route('/users/<id>', methods=['GET'])
def show(id):
    get_single_user_query = "SELECT `users`.`id` as `user_id`, CONCAT(`users`.`first_name`,\" \", `users`.`last_name`) as `user_name`,  `users`.`email` as `email`, DATE_FORMAT(`users`.`created_at`, \"%M %D, %Y\") as `created_at` FROM `users` WHERE `users`.`id` = :field_one;"

    get_single_user_data = {'field_one' : id}

    user = mysql.query_db(get_single_user_query, get_single_user_data)
    return render_template('show.html', user=user[0])


# GET request to /users/new - calls the new method to display a form allowing users to create a new user.
@app.route('/users/new', methods=['GET'])
def new():
    return render_template('new.html')


# POST to /users/create - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created.
@app.route('/users/create', methods=['POST'])
def create():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]

    create_user_query = 'INSERT INTO `users` (`first_name`, `last_name`, `email`, `created_at`, `updated_at`) VALUES (:field_one, :field_two, :field_three, now(), now());'
    create_user_data = {
        'field_one': first_name,
        'field_two': last_name,
        'field_three': email,
    }

    create_user_result = mysql.query_db(create_user_query, create_user_data)
    user_id = create_user_result
    return redirect('/users/' + str(user_id))


# GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. Have this redirect back to /users once deleted.
@app.route('/users/<id>/destroy', methods=['POST'])
def destroy(id):
    delete_user_query = "DELETE FROM `users` WHERE `users`.`id` = :field_one;"
    delete_user_data = {'field_one' : id}

    user_delete = mysql.query_db(delete_user_query, delete_user_data)
    return redirect('/users')


if __name__ == '__main__':
    app.run(debug=True)