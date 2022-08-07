#!/usr/bin/python3
"""displays all values where name matches the argument"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states  WHERE name = '{}' ORDER BY id ASC"
                   .format(argv[4]))
    query_rows = cursor.fetchall()
    for row in query_rows:
        if (row[1] == argv[4]):
            print(row)
    cursor.close()
    conn.close()
