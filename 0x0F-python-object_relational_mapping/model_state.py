#!/usr/bin/python3

"""
Write a python file that contains the class definition of a State and an
instance Base = declarative_base()

"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == '__main__':
    from sqlalchemy import create_engine
    engine = create_engine('mysql+mysqldb://root:password@localhost:3306')
    Base.metadata.create_all(engine)
