#!/usr/bin/python3
"""A module for a script that list all states starting with N"""


def query():
    """Lists all states starting with N from database hbtn_0e_0_usa"""

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
    sql = "SELECT *\
            FROM states\
            WHERE name='{}'\
            ORDER BY id"
    cursor.execute(sql.format(STATE))
    query = cursor.fetchall()

    my_list = []
    for state in query:
        my_list.append(state)

    cursor.close()
    db.close()

    return my_list


def main():
    """Print all states starting with N"""
    my_list = query()
    for state in my_list:
        print(state)


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    main()
