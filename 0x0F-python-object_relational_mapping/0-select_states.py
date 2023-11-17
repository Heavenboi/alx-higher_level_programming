#!/usr/bin/python3
""" script that lists all states from database hbtn_0e_0_usa"""

import MySQLdb
import sys

def main():
    conn = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        usr = sys.argv[1],
        passwd = sys.argv[2],
        db = sys.argv[3],
        charset = "utf8"
    )

    cur = conn.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)
    states = cur.fetchall()
    for i in states:
        print(i)
    cur.close()
    connect.close()

    if __name__ == "__main__"
