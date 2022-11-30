from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/')
def index():
    return 'Index Page'

class Row()
@app.route('/mihkelTest/<int:post_id>')
def getTested(post_id):
    rows = [{ 'message': 'Foo' }, { 'message': 'Bar' }]
    return render_template('mihkelTest.html', rows=rows)