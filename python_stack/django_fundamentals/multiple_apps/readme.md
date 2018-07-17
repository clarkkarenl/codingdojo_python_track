Assignment: Multiple Apps
Karen Clark
2018-07-16

Objectives
* Get familiar with setting multiple Django apps

With Django, it's easy to create multiple apps that can be used across multiple projects.  Let's say that you're a freelancer and have worked with many clients in the past.  Say that the particular industry your clients are in, almost every single project you've worked on, every client/project wants their own blogs, surveys, and user management system.  Instead of having to re-create these modules each time from scratch, you decide to create three independent apps that you can use throughout all of these projects.

Using what you've learned, please build the following from your previous Django App assignment:

* Create two additional apps: surveys and users.
* Have the following URL either display a simple HttpResponse or redirect to a different URL for the following apps
** blogs app
*** /blogs - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'.
*** /blogs/new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'.
*** /blogs/create - Have this be handled by a method named 'create'.  For now, have this url redirect to /blogs.
*** /blogs/{{number}} - display 'placeholder to display blog {{number}}.  For example /blogs/15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'.
*** /blogs/{{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'.
*** /blogs/{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /blogs. 
** surveys app
*** /surveys - display "placeholder to display all the surveys created"
*** /surveys/new - display "placeholder for users to add a new survey
** users app
*** /register - display 'placeholder for users to create a new user record'
*** /login - display 'placeholder for users to login' 
*** /users/new - have the same method that handles /register also handle the url request of /users/new
*** /users - display 'placeholder to later display all the list of users'

Have the root route (e.g. localhost/) be handled by the index method in the blogs' view file.