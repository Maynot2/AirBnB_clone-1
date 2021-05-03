#!/usr/bin/python3
"""
    A simple flask exemple
"""

from web_flask import app


@app.route('/', strict_slashes=False)
def hello():
    """Says Hello on the home page"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
