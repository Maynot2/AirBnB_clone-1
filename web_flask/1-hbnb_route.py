"""
    A simple flask exemple with 2 routes
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
