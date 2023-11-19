#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the states
where name matches the argument but safe from MySQL injections.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = conn.cursor()
    search = sys.argv[4]
    query = """SELECT * FROM states WHERE name = '{:s}' ORDER BY id ASC""".format(
        search)
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        if state[1] == search:
            print(state)
    cursor.close()
    conn.close()
