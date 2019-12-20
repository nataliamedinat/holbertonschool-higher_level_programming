#!/usr/bin/python3
""" Class that gets the content of the table """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    session = Session(engine)
    first_state = session.query(State).filter_by(id='1').first()
    if first_state:
        print("{}: {}".fomrat(first_state.id, first_state.name))
    else:
        print("Nothing")
    session.close()
