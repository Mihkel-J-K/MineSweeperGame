from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/')
def index():
    return render_template('titleScreen.html')

@app.route('/mihkelTest')
def getTested():
    rows = []
    for i in range(25):
        rows += [[]]
        for j in range(25):
            rows[i] += [random.randint(0,8)]

    return render_template('mihkelTest.html', matrix=rows)