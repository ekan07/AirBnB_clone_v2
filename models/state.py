#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """Return the list of City instances corresponding to this state"""
            from models import storage
            my_cities = storage.all(City)
            state_city = [cc for cc in my_cities.values()
                          if cc.state_id == self.id]
            return state_city
