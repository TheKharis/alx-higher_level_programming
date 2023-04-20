#!/usr/bin/python3

"""
A script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa

"""

import sys
import MySQLdb

if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # connect to database
    try:
        db = MySQLdb.connect(host="localhost", user=mysql_username,
                             passwd=mysql_password, db=database_name,
                             port=3306)
        cur = db.cursor()
        # Execute query search
        query = """SELECT cities.id, cities.name, states.name FROM cities
        JOIN states ON cities.state_id = states.id WHERE states.name = %s
        ORDER BY cities.id ASC"""

        cur.execute(query, (state_name,))

        cities = cur.fetchall()

        # print results
        for city in cities:
            print(city)

    except MySQLdb.Error as e:
        print(f"MySQL Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)
