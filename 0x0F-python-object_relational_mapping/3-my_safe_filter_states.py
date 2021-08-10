#!/usr/bin/python3
"""A module for a script that list all states starting with N"""


def query():
    """A script that takes in arguments and displays
    all values in the states table of hbtn_0e_0_usa
    where name matches the argument"""

    USER = argv[1]
    PASS = argv[2]
    DATABASE = argv[3]
    STATE = argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=USER,
                         passwd=PASS,
                         database=DATABASE)
    cursor = db.cursor()
    sql = "SELECT id, name\
            FROM states\
            WHERE BINARY name=%s\
            ORDER BY id"
    cursor.execute(sql, (STATE,))
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
