# Assignment: Landing Page
# Karen Clark
# 2018-06-09
#
# Assignment: Landing Page
# Create a flask project capable of handling the following routes.
# localhost:5000/
# This route should serve a view file called index.html and
# display a greeting. This will be considered our 'root route'.
# localhost:5000/ninjas
# This route should serve a view file called ninjas.html and
# display information about ninjas.
# localhost:5000/dojos/new
# This route should serve a view file called dojos.html and
# have a form.
# Next Steps
# Create a folder inside of your project labeled static.


from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')


@app.route('/dojos')
def dojos():
    return render_template('dojos.html')


@app.route('/dojos/new', methods=['POST'])
def dojos_new():
    name = request.form['name']
    fav_ninja = request.form['ninja']

    return redirect('/ninjas')


app.run(debug=True)