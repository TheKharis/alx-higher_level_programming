#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

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
        cur = db.cursor()
    except MySQLdb.Error as e:
        print(f"MySQL Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)

    # Execute query search
    try:
        query = """SELECT cities.id, cities.name, states.name FROM cities JOIN
        states ON cities.state_id = states.id ORDER BY cities.id ASC"""

        cur.execute(query)

        cities = cur.fetchall()
    except MySQLdb.Error as e:
        print(f"MySQL Error {e.args[0]}: {e.args[1]}")

    # print results
    for city in cities:
        print(city)

    # clean up
    cur.close()
    db.close()
