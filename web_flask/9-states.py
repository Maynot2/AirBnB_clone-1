#!/usr/bin/python3
"""
    A simple flask exemple
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Displays all the states"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<string:id>', strict_slashes=False)
def given_state(id):
    """Display a given state with its cities"""
    key = 'State.{}'.format(id)
    state = storage.all(State).get(key)
    return render_template('9-states.html', states=state)


@app.teardown_appcontext
def rm_sqlalchemy_sess(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
