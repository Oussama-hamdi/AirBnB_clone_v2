#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display a messages when the root url is accessed"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Display a messages when /hbnb url is accessed"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Display C followed by the value of text"""
    return "C " + text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """Display Python followed by the value of text"""
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Display n is a number only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display a HTML page with a number if n is integer"""
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display a HTML page indicating if n is odd or even"""
    odd_even = "odd" if n % 2 else "even"
    file_name = "6-number_odd_or_even.html"
    return render_template(file_name, number=n, odd_even=odd_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
