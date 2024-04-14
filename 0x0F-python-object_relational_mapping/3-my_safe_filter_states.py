#!/usr/bin/python3
"""
This script takes an argument and displays all values
in the 'states' table where the 'name' column matches
the argument from the database 'hbtn_0e_0_usa'.

This version of the script uses parameterized queries
to prevent SQL injection.ipt is safe from
MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Main entry point of the script.
    Retrieves and displays states from the database
    based on the provided argument.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {
            'name': argv[4]
        })

        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
