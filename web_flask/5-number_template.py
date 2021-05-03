"""
    A simple flask exemple with 3 routes
"""

from web_flask import app
from flask import render_template


@app.route('/', strict_slashes=False)
def hello():
    """Says Hello on the home page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to HBNB page"""
    return 'HBNB'


@app.route('/c/<path>', strict_slashes=False)
def c_is(path):
    """Route to /c/catch_all"""
    return 'C {}'.format(path.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<path>', strict_slashes=False)
def python_is(path='is cool'):
    """Multiple routes to python_is"""
    return 'Python {}'.format(path.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
        Displays number to matching route
        only if n can be converted to a number
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """
        Displays number to matching route
        only if n can be converted to a number
    """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)