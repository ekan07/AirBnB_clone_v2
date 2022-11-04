#!/usr/bin/python3
"""
a script that starts a Flask web application in which
one route accepts user input
"""
from flask import Flask
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
def message(text):
    '''Display "C" followed by the text variable'''
    text = text.replace('_', ' ')
    return 'C %s' % text


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
