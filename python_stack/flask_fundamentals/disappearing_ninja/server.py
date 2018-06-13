# Assignment: Disappearing Ninja
# Karen Clark
# 2018-06-12

# Assignment: Disappearing Ninja
# Build a flask application with the below functionality.
# These are the routes that you need to set up:

# On the default page ('localhost:5000'), it should display 
# a view that says "No ninjas here"
# When user visits /ninja, it should display all four Ninja 
# Turtles (Leonardo, Michelangelo, Raphael, and Donatello)
# /ninja/[ninja_color], should display the corresponding Ninja 
# Turtle (grab the color parameter out of the requested URL)
# If user visits /ninja/blue, it should only display the Ninja 
# Turtle Leonardo.
# /ninja/orange - Ninja Turtle Michelangelo.
# /ninja/red - Ninja Turtle Raphael
# /ninja/purple - Ninja Turtle Donatello
# If a user tries to hack into your web app by specifying a 
# color or string combination other than the colors (Blue, 
#     Orange, Red, and Purple), example: /ninja/black or 
# /ninja/123, then display the image notapril.jpg

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def get_ninjas(color):
    poss_colors = ['blue', 'red', 'orange', 'purple']
    return render_template('colors.html', color = color, poss_colors = poss_colors)


app.run(debug=True)