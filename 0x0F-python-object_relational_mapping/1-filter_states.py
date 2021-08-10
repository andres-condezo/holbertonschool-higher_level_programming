#!/usr/bin/python3
"""A module for a script that list all states starting with N"""


def query():
    """Lists all states starting with N from database hbtn_0e_0_usa"""

    USER = argv[1]
    PASS = argv[2]
    DATABASE = argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=USER,
                         passwd=PASS,
                         database=DATABASE)
    cursor = db.cursor()
    sql = "SELECT id, name\
            FROM states\
            WHERE name LIKE BINARY 'N%'"
    cursor.execute(sql)
    query = cursor.fetchall()

    my_list = []
    for state in query:
        my_list.append(state)

    cursor.close()
    db.close()

    return my_list


def main():
    """print all states in my_list"""
    my_list = query()
    if my_list is not None:
        for state in my_list:
            print(state)


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    main()
