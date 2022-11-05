from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/')
def index():
    return 'Index Page'

@app.route('/mihkelTest')
def getTested():
    return render_template('mihkelTest.html')