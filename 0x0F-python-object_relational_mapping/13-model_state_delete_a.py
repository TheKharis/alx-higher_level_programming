#!/usr/bin/python3
"""
This script will delete all State objs with a  name containing 'a'
from the db `hbtn_0e_6_usa`
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # create new engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    # delete State object
    query = session.query(State).filter(State.name.like('%a%'))
    for state in query:
        session.delete(state)
    # commit and close session
    session.commit()
    session.close()
