#!/usr/bin/python3
""" Base class """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ All information about state table """

    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
