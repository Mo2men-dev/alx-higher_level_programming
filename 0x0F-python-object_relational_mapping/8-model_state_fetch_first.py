#!/usr/bin/python3
"""a select query using SQLA
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def create_session():
    """makes a select query
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        res = session.query(State).first()
        print("{}: {}".format(res.id, res.name))
    except Exception as e:
        raise Exception("Couldn't excute query", e)
    finally:
        session.close()
        return 0


if __name__ == "__main__":
    create_session()
