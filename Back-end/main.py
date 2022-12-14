from flask import Flask, render_template
import random
from mänguväli import *

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/')
def index():
    return render_template('titleScreen.html')


@app.route('/theGame')
def Main():
    global mänguväli
    global kaetudMänguväli
    mänguväli = genereeri_mänguväli(30, 30, 150)
    kaetudMänguväli = genereeri_mänguväli(30, 30, 0, "a")
    return render_template('theGame.html', matrix=kaetudMänguväli)

@app.route('/theGame/<int:index_i>/<int:index_j>')
def loading(index_i, index_j):
    print(index_j, index_i)
    global kaetudMänguväli
    global mänguväli
    kaetudMänguväli = avalda(index_i, index_j, kaetudMänguväli, mänguväli)
    return render_template('theGame.html', matrix=kaetudMänguväli)

@app.route('/theGame/flag/<int:index_i>/<int:index_j>')
def flag(index_i, index_j):
    print(index_j, index_i)
    global kaetudMänguväli
    if kaetudMänguväli[index_i][index_j] == 10:
        kaetudMänguväli[index_i][index_j] = 'a'
    else:
        kaetudMänguväli[index_i][index_j] = 10
    return render_template('theGame.html', matrix=kaetudMänguväli)
