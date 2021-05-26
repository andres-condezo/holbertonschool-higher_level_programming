#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, column in enumerate(row):
            print("{:d}".format(column), end="")
            if index < len(row) - 1:
                print(" ".format(column), end="")
        print()
