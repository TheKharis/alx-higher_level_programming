#!/usr/bin/python3
"""This script will create an SQL database and query data from the db"""

import MySQLdb
import sys

# Get command line arguments
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

# Connect to MySQL server
db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=mysql_username,
    passwd=mysql_password,
    db=database_name)

# Create a cursor object to execute queries
cursor = db.cursor()

# Execute the query to get all states
cursor.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all rows and print them
states = cursor.fetchall()
for state in states:
    print(state)

# Close the database connection
db.close()
