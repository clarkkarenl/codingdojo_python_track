from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", phrase='Knights of Ni!', times=5)
app.run(debug=True)
