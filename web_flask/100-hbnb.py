"""
    A simple flask exemple
"""

from web_flask import app
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


@app.template_filter('pluralize')
def pluralize(number, singular = '', plural = 's'):
    if number == 1:
        return '{} {}'.format(number, singular)
    else:
        return '{} {}'.format(number, plural)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays the home page"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb.html',
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def rm_sqlalchemy_sess(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
