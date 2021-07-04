#!/usr/bin/python3
"""my_calculator module"""


def main():
    """Main function"""
    dic_op = {"+": add, "-": sub, "*": mul, "/": div}

    if len(argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]

    if operator not in dic_op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    result = dic_op[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    main()
