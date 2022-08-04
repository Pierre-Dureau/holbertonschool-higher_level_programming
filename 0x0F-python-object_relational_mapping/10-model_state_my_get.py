#!/usr/bin/python3
"""prints the State object with the name passed as argument"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).filter(State.name == argv[4]).first()
    if (state):
        print(f"{state.id}")
    else:
        print('Nothing')
    session.close()
