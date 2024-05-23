#!/usr/bin/python3
"""displays the states based on args
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
        raise e("couldn't conncet to db")

    c = db.cursor()
    c.execute('SELECT * FROM states')
    arr = c.fetchall()
    for e in arr:
        if e[1] == state_name:
            print(e)


if __name__ == "__main__":
    connect_db()
