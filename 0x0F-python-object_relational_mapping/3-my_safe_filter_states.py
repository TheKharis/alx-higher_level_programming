#!/usr/bin/python3
"""
A script that takes in an argument and displays all values matching
argument, safe from injections

"""

import sys
import MySQLdb

if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # connect to database
    try:
        db = MySQLdb.connect(host="localhost",
                             user=mysql_username,
                             passwd=mysql_password,
                             db=database_name,
                             port=3306)
        cur = db.cursor()
    except MySQLdb.Error as e:
        print(f"MySQL Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)

    # Execute query search
    try:
        query = """SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY
        states.id"""

        cur.execute(query, (state_name_searched,))

        results = cur.fetchall()
    except MySQLdb.Error as e:
        print(f"MySQL Error {e.args[0]}: {e.args[1]}")

    # print results
    for row in results:
        print(row)

    # clean up
    cur.close()
    db.close()
