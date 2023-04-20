#!/usr/bin/python3

"""
Write a python file that contains the class definition of a State and an
instance Base = declarative_base()

"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

stateMeta = MetaData()  # parameterize metadata for modular use

Base = declarative_base(metadata=stateMeta)  # create Base instance


class State(Base):
    """Creates an instance of State
    Args:
        id(int): id of state
        name(str): name of state
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)
