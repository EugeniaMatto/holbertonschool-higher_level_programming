#!/usr/bin/python3
"""takes in an argument and displays all values in the states"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name \
                FROM states JOIN cities ON state_id=states.id \
                WHERE states.name LIKE %s ORDER BY cities.id",
                (argv[4],))
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    cur.close()
    db.close()
