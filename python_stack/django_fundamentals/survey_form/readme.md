Assignment: Survey Form
Karen Clark
2018-07-09

Build out the below wireframe in a new Django project with a new app called 'surveys'.

Start a new project from scratch this time. This will help you to:

1. Reinforce the important concepts you want to master
2. Get you to build things a lot faster as each iteration will help you optimize your workflow

For any web app, it’s critical that you understand how a form can be submitted and how POST, as well as session, data work. As you build the app described below, make sure you feel very comfortable with how information can be relayed between a form and controller/view (found in views.py currently), and how session and POST data are being handled.


Good Practice
For this assignment:

Do not have a single URL handle BOTH the POST submission as well as render the view file.
* For example, the form that’s rendered from http://localhost should be submitted not to /result but to /surveys/process. The method that handles /surveys/process should do all the logic, process POST data, manipulate session data and redirect to another URL, say /result.
* The reason we have a method to handle POST/session and another method to handle the view file is because it makes reading your code much easier.
* Also, if the same URL handled both POST and the rendering of the view when you reload that page, it would resubmit the form data. This is not good and is often a common mistake made by a rookie developer. 
How to do this in Django?

In your controller/view file (named views.py), be sure to import redirect along with render.

```
# Inside views.py
from django.shortcuts import render, HttpResponse, redirect
```

You can use redirect like so:
```
def runThis():
  return redirect('/')
```