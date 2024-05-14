#!/usr/bin/python3
"""
list all states starting with 'N'
"""

import MySQLdb
import sys

def get_states():
    """
    same as module doc
    """
    usr, pw, name = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        db = MySQLdb.connect('localhost', usr, pw, name)
    except Exception as err:
        raise err("couldn't connect to db")

    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
    arr = c.fetchall()
    for e in arr:
        print(e)

if __name__ == '__main__':
    get_states()
