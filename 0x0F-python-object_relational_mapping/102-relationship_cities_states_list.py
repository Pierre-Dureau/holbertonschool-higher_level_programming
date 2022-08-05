#!/usr/bin/python3
"""lists all City objects, and corresponding State objects"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for city in session.query(City).order_by(City.id).all():
        print(f"{city.id}: {city.name} -> {city.state.name}")
    session.close()
