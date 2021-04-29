"""
    A simple flask exemple with 3 routes
"""

from web_flask import app


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
