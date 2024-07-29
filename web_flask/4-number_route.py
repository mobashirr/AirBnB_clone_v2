#!/usr/bin/python3
"""
A script that starts a Flask web application:
- The application listens on 0.0.0.0, port 5000.
- Routes:
  - /: display “Hello HBNB!”
  - /hbnb: display “HBNB”
  - /c/<text>: display “C ” followed by the value of the text variable (replace underscores with spaces)
  - /python/(<text>): display “Python ” followed by the value of the text variable (replace underscores with spaces). The default value of text is “is cool”.
  - /number/<n>: display “n is a number” only if n is an integer.
- Uses the option strict_slashes=False in the route definition.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' when accessing the root route.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' when accessing the /hbnb route.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays 'C ' followed by the value of the text variable,
    with underscores replaced by spaces.
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Displays 'Python ' followed by the value of the text variable,
    with underscores replaced by spaces. The default value of text is “is cool”.
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays “n is a number” only if n is an integer.
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
