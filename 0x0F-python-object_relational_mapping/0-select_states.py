#!/usr/bin/python3
"""
This script connects to a MySQL database
and retrieves all states from the `states` table
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
	Main entry point of the script.
	Connects to the MySQL database and retrieves
	the states from the `states` table.
	"""
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    # Execute the SQL query to select all states
    cur.execute("SELECT * FROM states")

    # Fetch all rows returned by the query
    rows = cur.fetchall()

    # Print each row (state information)
    for row in rows:
        print(row)
