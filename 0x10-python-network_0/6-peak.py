#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    beg = 0
    end = len(list_of_integers)-1

    if list_of_integers[beg] > list_of_integers[beg+1]:
        return list_of_integers[beg]
    if list_of_integers[end] > list_of_integers[end-1]:
        return list_of_integers[end]

    mid = (beg+end)//2
    if list_of_integers[mid-1] < list_of_integers[mid] and list_of_integers[mid+1] < list_of_integers[mid]:
        return list_of_integers[mid]
    if list_of_integers[mid] < list_of_integers[mid-1]:
        return find_peak(list_of_integers[beg:mid+1])
    elif list_of_integers[mid] < list_of_integers[mid+1]:
        return find_peak(list_of_integers[mid:end+1])
    else:
        return list_of_integers[beg]
