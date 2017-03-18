#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base


class State(BaseModel):
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref=backref(
            "state", cascade="all, delete-orphan"))
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            all_cities = storage.all("City").values()
            return (city for city in all_cities if city.state_id == self.id)
