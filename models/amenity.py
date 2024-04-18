#!/usr/bin/python3
"""Amenity Module for HBNB project"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Amenity class for storing information about amenities"""

    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
