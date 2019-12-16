#!/usr/bin/python3
# Lists all states from the database
import MySQLdb
import sys

if __name__ == "__main__":
    # Connection
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    # Executing queries
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                ORDER BY states.id ASC", (sys.argv[4]))

    # To obtain results
    res = cur.fetchall()
    for row in res:
        print(row)

    # Clean up cur and data
    cur.close()
    db.close()
