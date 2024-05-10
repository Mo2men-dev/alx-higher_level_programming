#!/usr/bin/python3
"""list all states from a database"""

import sys
import MySQLdb

def connect_sql():
    """
    connect to sql server
    """
    try:
        cnct = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    except Exception as e:
        raise("couldn't connect to sql server")
        return 0

    cur = cnct.cursor()
    cur.execute('select * from states order by states.id')
    arr = cur.fetchall()
    for data in arr:
        print(data)

if __name__ == '__main__':
    connect_sql()
