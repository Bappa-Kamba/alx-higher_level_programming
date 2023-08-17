#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    c_set = []

    for i in set_1:
        if i not in set_2:
            c_set.append(i)

    for i in set_2:
        if i not in set_1:
            c_set.append(i)
    return c_set
