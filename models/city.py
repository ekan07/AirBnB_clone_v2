#!/usr/bin/python3
"""This is the city class"""
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv


class City(BaseModel, Base):
    """The city class
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place",
                              backref="cities",
                              cascade="all, delete, delete-orphan")
