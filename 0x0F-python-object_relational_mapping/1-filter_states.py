#!/usr/bin/python3
"""
This script retrieves and prints all states
whose name starts with the letter 'N'
from the MySQL database 'hbtn_0e_0_usa'
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Main entry point of the script.
    Retrieves states with names starting with 'N'
    from the 'states' table in the database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
