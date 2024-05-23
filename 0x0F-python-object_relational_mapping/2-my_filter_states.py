#!/usr/bin/python3
"""displays values from args
"""

import sys
import MySQLdb


args = sys.argv
usr, pw, name = args[1], args[2], args[3]
state_name = args[4]

try:
    db = MySQLdb.connect('localhost', usr, pw, name)

except Exception as e:
    raise("couldn't conncet to db")

c = db.cursor()
c.execute("SELECT * FROM states WHERE name = \'{}\'".format(state_name))
arr = c.fetchall()
for e in arr:
    print(e)
