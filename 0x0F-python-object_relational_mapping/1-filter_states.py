#!/usr/bin/python3
"""A script that lists all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == '__main__':

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # connect to database
    try:
        db = MySQLdb.connect(host="localhost",
                             user=mysql_username,
                             passwd=mysql_password,
                             db=database_name,
                             port=3306)
        # create cursor
        cur = db.cursor()
    except MySQLdb.Error as e:
        print(f"MySQLdb Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)

    try:
        query = """SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY
        states.id"""
        # Execute query
        cur.execute(query)
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        print(f"MySQLdb Error {e.args[0]} : {e.args[1]}")

    # print results
    for row in rows:
        print(row)

    # close all connections
    cur.close()
    db.close()
