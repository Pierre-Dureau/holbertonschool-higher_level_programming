#!/usr/bin/python3
"""lists all cities of a state"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cursor = conn.cursor()
    cursor.execute("SELECT cities.name FROM cities \
        INNER JOIN states ON cities.state_id=states.id \
        WHERE states.name = '{:s}'".format(argv[4]))
    query_rows = cursor.fetchall()
    print(*(row[0] for row in query_rows), sep=', ', end='\n')
    cursor.close()
    conn.close()
