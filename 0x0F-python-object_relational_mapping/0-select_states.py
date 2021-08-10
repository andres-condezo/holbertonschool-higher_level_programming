#!/usr/bin/python3
"""a module for a script that list all states"""


def query():
    """a script that lists all states from the database hbtn_0e_0_usa"""

    USER = argv[1]
    PASS = argv[2]
    DATABASE = argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=USER,
                         passwd=PASS,
                         database=DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id")
    query = cursor.fetchall()

    my_list = []
    for state in query:
        my_list.append(state)

    cursor.close()
    db.close()

    return my_list


def main():
    my_list = query()
    if my_list is not None:
        for state in my_list:
            print(state)


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    main()
