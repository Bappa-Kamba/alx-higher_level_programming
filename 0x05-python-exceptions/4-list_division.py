#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    while i < list_length:
        try:
            res = my_list_1[i] / my_list_2[i]
            new_list.append(res)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
            continue
        except TypeError:
            print("wrong type")
            new_list.append(0)
            continue
        except IndexError:
            print("out of range")
            new_list.append(0)
            continue
        finally:
            i += 1
    return new_list
