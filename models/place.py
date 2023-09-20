#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


place_amenity = Table(
             'place_amenity',
             Base.metadata,
             Column('place_id', String(60),
                    ForeignKey('places.id'), nullable=False),
             Column('amenity_id', String(60),
                    ForeignKey('amenities.id'), nullable=False)
             )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates='place_amenities')

    @property
    def reviews(self):
        """ getter attribute of reviews"""
        rev_list = []
        for review in reviews:
            if review.place_id == self.id:
                rev_list.append(review)
        return rev_list

    @property
    def amenities(self):
        """ getter/setter for amenities"""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj=None):
        """setter of amenities"""
        if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
            self.amenity_ids.append(obj.id)
