#!/usr/bin/python3
"""A module for a script that list all states starting with N"""


def query():
    """A script that lists all cities from the database hbtn_0e_4_usa"""

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
    sql = "SELECT cities.name\
            FROM cities\
            INNER JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id"
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
    cities_names = []
    for state in my_list:
        cities_names.append(state[0])
    print(", ".join(cities_names))


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    main()
