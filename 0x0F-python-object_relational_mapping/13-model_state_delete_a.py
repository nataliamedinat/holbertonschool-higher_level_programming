#!/usr/bin/python3
"""deletes all State objects with a name containing the
letter a from the database
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)

    states = session.query(State).filter(State.name.like("%a%")).all()
    if states:
        for state in states:
            session.delete(state)
        session.commit()
    session.close()
