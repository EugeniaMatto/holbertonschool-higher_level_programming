#!/usr/bin/python3
""" ex 0 """

if __name__ == "__main__":
    import sys
    import MySQLdb
    av = sys.argv
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=av[1], passwd=av[2], db=av[3])
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE name LIKE '{av[4]}' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
