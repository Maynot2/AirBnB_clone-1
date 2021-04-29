"""
    A simple flask exemple with 3 routes
"""

from web_flask import app
from flask import render_template
from models import storage
from models.state import State


@app.route('/states_list', strict_slashes=False)
def template():
    """Displays all the states currently defined in storage"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def rm_sqlalchemy_sess(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
