#!/usr/bin/python3
# Cities by states

import MySQLdb
import sys

if __name__ == "__main__":
    # Connection
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    # Executing queries
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
    FROM cities, states\
    WHERE cities.state_id = states.id\
    ORDER BY cities.id ASC")

    # To obtain results
    res = cur.fetchall()
    for row in res:
        print(row)

    # Clean up
    cur.close()
    db.close()
