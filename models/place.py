#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id',
                                 String(60), ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id',
                                 String(60), ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """Place class
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review",
                               backref="place",
                               cascade="all, delete-orphan")

        amenities = relationship("Amenity",
                                 secondary='place_amenity',
                                 backref="place_amenities",
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """Returns a list of 'Review' instances for this place"""
            from models import storage
            all_reviews = storage.all(Review)
            return [review for review in all_reviews.values()
                          if review.place_id == self.id]

        @property
        def amenities(self):
            """Return a list of 'Amenity' instances for this place"""
            from models import storage
            all_amenities = storage.all(Amenity)
            return [amenity for amenity in all_amenities.values()
                            if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            """Add amenity id of amenity available at this place
            in amenity_ids
            """
            if (type(value) is Amenity):
                self.amenity_ids.append(value.id)
