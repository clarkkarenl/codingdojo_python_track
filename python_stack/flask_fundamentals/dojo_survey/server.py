# Assignment: Dojo Survey
# Karen Clark
# 2018-06-11

# Assignment: Dojo Survey
# Build a flask application that accepts a form submission, 
# redirects, and presents the submitted data on a results page.
# Hint: Although we've told you never to render from a post 
# route, you'll need to do so for this assignment. We'll show 
# you tools to avoid doing so soon.

from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def gather_data():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result = result)
    else:
        return render_template('result.html')


app.run(debug=True)
