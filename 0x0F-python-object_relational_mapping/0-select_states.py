#!/usr/bin/python3
""" script that lists all states from database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3]
                                 )

    cur = connection.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)
    [print(state) for state in cur.fetchall()]
