#!/usr/bin/python3
"""a select query using SQLA
"""

import sys.argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
    argv[1], argv[2], argv[3]), pool_pre_ping=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))

session.close()
