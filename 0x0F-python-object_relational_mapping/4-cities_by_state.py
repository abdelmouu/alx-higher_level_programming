#!/usr/bin/python3
"""
This script retrieves and lists all cities from
the 'cities' table in the database 'hbtn_0e_4_usa',
along with their corresponding state names.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Main entry point of the script.
    Retrieves cities with their corresponding state
	names from the database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY
                cities.id ASC
        """)

        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
