#!/usr/bin/python3
"""A script that lists all cities from the database given"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    match = sys.argv[4]
    cur.execute("""
        SELECT cities.name
        FROM cities
        INNER JOIN states ON states.id=cities.state_id
        WHERE states.name = %s
        """, (match,))
    rows = cur.fetchall()
    tmp = [row[0] for row in rows]
    print(*tmp, sep=", ")
    cur.close()
    db.close()
