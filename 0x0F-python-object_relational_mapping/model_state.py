#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

a = sys.argv
if __name__ == "__main__":
    e = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                a[1], a[2], a[3]), pool_pre_ping=True)
    Base.metadata.create_all(e)
