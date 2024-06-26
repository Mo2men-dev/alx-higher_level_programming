#!/usr/bin/python3
"""list all cities from a database"""

import sys
import MySQLdb


def sql_connect():
    """connect to sql server
    """
    try:
        connection = MySQLdb.connect(
                'localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    except Exception as err:
        raise err("can't connect to sql server")
        return 0
    curse = connection.cursor()
    curse.execute('''SELECT cities.id, cities.name, states.name
            FROM cities INNER JOIN states
            ON states.id = cities.state_id
            ORDER BY cities.id''')
    arr = curse.fetchall()
    for data in arr:
        print(data)


if __name__ == '__main__':
    sql_connect()
