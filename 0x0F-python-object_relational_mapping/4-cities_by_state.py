#!/usr/bin/python3
"""A module for a script that list all states starting with N"""


def query():
    """A script that lists all cities from the database hbtn_0e_4_usa"""

    USER = argv[1]
    PASS = argv[2]
    DATABASE = argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=USER,
                         passwd=PASS,
                         database=DATABASE)
    cursor = db.cursor()
    sql = "SELECT cities.id, cities.name, states.name\
            FROM cities\
            INNER JOIN states\
            ON cities.state_id = states.id\
            ORDER BY cities.id"
    cursor.execute(sql)
    query = cursor.fetchall()

    my_list = []
    for state in query:
        my_list.append(state)

    cursor.close()
    db.close()

    return my_list


def main():
    """Print all states"""
    my_list = query()
    for state in my_list:
        print(state)


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    main()
