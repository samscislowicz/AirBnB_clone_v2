#!/usr/bin/python3
from flask import Flask
from flask import render_template
import sys
import os
from models import storage
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

app = Flask(__name__)


@app.route('/states_list')
def states():
    return render_template('7-states_list.html',
                           states=storage.all(State).values())


@app.route("/cities_by_states")
def cities_by_states():
    return render_template('8-cities_by_states.html',
                           states=storage.all(State).values())

@app.route("/states")
def state_and_states():
    return render_template('9-states.html',
                           states=storage.all(State).values(),
                           selected="Only")

@app.route('/states/<id>')
def cities_stateid():
    return


@app.teardown_appcontext
def end_sesh(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
