#!/usr/bin/python3
""" State Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")


    def __init__(self, *args, **kwargs):
        """ init state """
        super().__init__(*args, **kwargs)


    if models.storage_type != "db":
        @property
        def cities(self):
            """ list cities """
            list_city = []
            all_inst_c = models.storage.all(City)
            for value in all_inst_c.values():
                if value.state_id == self.id:
                    list_city.append(value)
            return list_city

