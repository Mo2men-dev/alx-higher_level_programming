#!/usr/bin/python3
"""get cities based on state
"""

import sys
import MySQLdb


def connect_db():
    """connects to the db
    """
    args = sys.argv
    usr, pw, name = args[1], args[2], args[3]
    state_name = args[4]
    try:
        db = MySQLdb.connect('localhost', usr, pw, name)
    except Exception as e:
        raise e("couldn't connect to db")

    c = db.cursor()
    c.execute("""
            SELECT cities.name
            FROM cities INNER JOIN states
            ON cities.state_id = states.id
            WHERE states.id = (SELECT states.id FROM states
            WHERE states.name = \'{}\')""".format(state_name))

    arr = c.fetchall()

    if len(arr) == 0:
        print()
        return

    for i, e in enumerate(arr):
        if i != len(arr) - 1:
            print(e[0], end=", ")
        else:
            print(e[0])


if __name__ == "__main__":
    connect_db()
