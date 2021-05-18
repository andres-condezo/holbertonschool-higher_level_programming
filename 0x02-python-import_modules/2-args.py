#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    args = len(argv) - 1
    i = 1

    print("{:d} argument{}{}"
          .format(
              args,
              "s" if args != 1 else "",
              "." if args == 0 else ":"
          ))

    for arguments in range(args):
        print("{:d}: {}".format(i, argv[i]))
        i = i + 1
