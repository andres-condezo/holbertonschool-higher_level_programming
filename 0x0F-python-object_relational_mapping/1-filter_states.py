#!/usr/bin/python3
"""A module for a script that list all states starting with N"""


def main():
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
    cursor.execute(
        "SELECT * FROM states WHERE SUBSTRING(name,1,1) = 'N' ORDER BY id")
    query = cursor.fetchall()

    for state in query:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    main()
