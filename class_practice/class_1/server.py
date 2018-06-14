from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    my_students = [ 
    {'name' :'karen', 'location': 'seattle'},
    {'name' :'daman', 'location': 'seattle'},
    {'name' :'bianca', 'location': 'seattle'},
    {'name' :'sahal', 'location': 'seattle'}]
    return render_template('index.html', name = "KAREN", students = my_students)

@app.route('/hello')
def hello_world():
    return "hello world"

@app.route('/process_data', methods=['POST'])
def process():
    print request.form(['first_name'])
    return redirect('/')

app.run(debug=True)