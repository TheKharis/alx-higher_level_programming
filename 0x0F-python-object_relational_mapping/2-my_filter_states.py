#!/usr/bin/python3
"""A script that takes in an argument and displays all values"""

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
        print(f"Error connecting to MySQL db {e}")
        sys.exit(1)

    # Execute query search
    try:
        sql_query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY
        id".format(state_name_searched)

        cur.execute(sql_query)

        results = cur.fetchall()
    except MySQLdb.Error as e:
        print("Error executing query {e}")

    # print results
    for row in results:
        print(row)

    # clean up
    cur.close()
    db.close()
