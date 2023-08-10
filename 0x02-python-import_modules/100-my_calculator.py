#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    f = {"+": add, "-": sub, "*": mul, "/": div}

    if operator not in f:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, f[operator](a, b)))
