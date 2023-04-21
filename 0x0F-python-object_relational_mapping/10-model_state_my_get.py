#!/usr/bin/python3
"""
A script that prints the State object with the name passed as argument from the
database hbtn_0e_6_usa

"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Setup engine and session
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create tables
    Base.metadata.create_all(engine)

    # Execute query
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state:
        print(state.id)
    else:
        print('Not found')

    # Close the session
    session.close()
