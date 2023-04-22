#!/usr/bin/python3
"""
This script will change the name of a State obj from the db `hbtn_0e_6_usa`
The state with id = 2 will be changed to New Mexico
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

    # change State object
    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = 'New Mexico'
        session.commit()
    # close session
    session.close()
