#!/usr/bin/python3
"""prints all City objects from"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_city import Base, City
from model_state import State
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for city, state in session.query(City, State)\
    .where(City.state_id == State.id).order_by(City.id).all():
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()

