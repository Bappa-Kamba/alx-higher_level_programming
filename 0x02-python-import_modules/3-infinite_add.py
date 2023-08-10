#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    count = len(argv)
    for i in range(1, (count)):
        number = int(argv[i])
        sum += number
    print("{}".format(sum))
