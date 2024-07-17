#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    import os
    HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
    if HBNB_TYPE_STORAGE == 'db':
        cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        from models import storage
        from models.city import City
        return [city for city in storage.all(City).values() if city.state_id == self.id]
