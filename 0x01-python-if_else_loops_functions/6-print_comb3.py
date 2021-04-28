#!/usr/bin/python3
for dec in range(10):
    for und in range(1, 10):
        if (dec <= und):
            if (dec != und):
                if (dec == 8 and und == 9):
                    print("{:d}{:d}".format(dec, und))
                else:
                    print("{:d}{:d}".format(dec, und), end=', ')
