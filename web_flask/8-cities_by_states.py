#!/usr/bin/python3
"""
    A simple flask exemple
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """Displays all cities in each states"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def rm_sqlalchemy_sess(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
