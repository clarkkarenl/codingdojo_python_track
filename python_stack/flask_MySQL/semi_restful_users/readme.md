Assignment: Semi-Restful Users
Karen Clark
2018-07-04

Create a web app that can handle all of the CRUD operations (create, read, update and destroy) for a table. Use your friends database for the following assignment.

But first, what does REST mean?
It's very common for a web application to provide the user interface for creating, reading, updating, or destroying a 'resource' (a table). For example, imagine you want to build a web application that allows the user to create/read/update/destroy users. There are many ways that you can build web applications like this. For example, you could have resources called users, products, pd (short for products) and so forth. You could also have different methods that essentially do the same thing. So, to display user information for user id 1, you could have the URL 'users/1' provide this info or 'users/show/1' or 'users/show_info/1' or 'users/display/1', etc.

Since many web applications perform CRUD operations, you can imagine how confusing this could get if everyone followed different conventions for creating routing and method names for these operations.

A REST or RESTful route is simply a set of route naming conventions that the industry has agreed to follow in order to make it easier to send requests to APIs. It's up to you whether you also follow these rules/conventions but we strongly encourage you to get familiar with the following rules for RESTful routing, as you may be making requests to, or someday creating your own, API.

Right now with Flask, it's not quite possible for you to do the full RESTful architecture, so the exercise below is to help you get somewhat familiar with RESTful routes. Later when you get into other stacks (such as MEAN or Rails), you'll already be somewhat familiar with REST concepts.

Make sure to...

Have 7 routes in your server.py. Because we are working with 'users', they might look like:
1. a GET request to /users - calls the index method to display all the users. This will need a template.
2. GET request to /users/new - calls the new method to display a form allowing users to create a new user. This will need a template.
3. GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an existing user with the given id. This will need a template.
4. GET /users/<id> - calls the show method to display the info for a particular user with given id. This will need a template.
5. POST to /users/create - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created.
6. GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. Have this redirect back to /users once deleted.
7. POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit. Have this redirect to /users/<id> once updated.

Notice that for every form submission we use a POST method, while we're rendering our templates from get routes.