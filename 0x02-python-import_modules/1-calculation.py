#!/usr/bin/python3
import calculator_1 as m
if __name__ == "__main__":
    a = 10
    b = 5
    print('{:d} + {:d} = {:d}'.format(a, b, m.add(a, b)))
    print('{:d} - {:d} = {:d}'.format(a, b, m.sub(a, b)))
    print('{:d} * {:d} = {:d}'.format(a, b, m.mul(a, b)))
    print('{:f} / {:f} = {:f}'.format(a, b, m.div(a, b)))
