#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    args = len(argv) - 1
    i = 1
    temp = 0

    for arguments in range(args):
        temp = temp + int(argv[i])
        i = i + 1

    print("{:d}".format(temp))
