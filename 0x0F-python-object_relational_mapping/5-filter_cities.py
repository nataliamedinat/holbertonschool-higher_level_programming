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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    INNER JOIN states ON cities.state_id = states.id\
    WHERE states.name = %s\
    ORDER BY cities.id ASC", (argv[4], ))

    c = []
    for row in cur.fetchall():
        c.append(row[1])
    print(", ".join(c))

    # Clean up
    cur.close()
    db.close()
