from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/')
def index():
    return render_template('titleScreen.html')


rows = []
for i in range(25):
    rows += [[]]
    for j in range(25):
        rows[i] += [random.randint(0,8)]

empty_rows = []
for i in range(25):
    empty_rows += [[]]
    for j in range(25):
        empty_rows[i] += [False]

@app.route('/theGame')
def Main():
    return render_template('theGame.html', matrix=empty_rows)

@app.route('/theGame/<int:index_i>/<int:index_j>')
def getTested(index_i, index_j):
    empty_rows[index_i][index_j] = rows[index_i][index_j]
    return render_template('theGame.html', matrix=empty_rows)

# @app.route('/theGame/<int:index_i>/<int:index_j>')
# def method_name(index_i, index_j):
#     print("LOCO")
#     pass
