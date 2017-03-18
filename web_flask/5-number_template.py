#!/usr/bin/python3
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hello_hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def hello_c():
    return 'C {}'.format(text.replace("_", " "))

@app.route('/python/')
@app.route('/python/<text>')
def hello_python(text="is cool"):
    return 'Python {}'.format(text.replace("_", " "))

@app.route('/number/<int:n>')
def number(n):
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>')
def number_template(n=None):
    return render_template('5-number.html', n=n)

if __name__=="__main__":
    app.run(host="0.0.0.0", port="5000")
