#!/usr/bin/python3
"""
a script that starts a Flask web application in which
one route accepts user input
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Displays "HBNB" '''
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_message(text):
    '''Display "C" followed by the text variable'''
    text = text.replace('_', ' ')
    return 'C %s' % text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_message(text='is cool'):
    '''Display "Python" followed by the text variable'''
    text = text.replace('_', ' ')
    return 'Python %s' % text


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    return "%d is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if <n> is an integer."""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
