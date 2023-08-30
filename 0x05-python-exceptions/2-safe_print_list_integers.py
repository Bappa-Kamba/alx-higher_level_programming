#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    p = 0
    while (i < x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                p += 1
            i += 1
        except (TypeError, ValueError):
            continue
    print()
    return p
