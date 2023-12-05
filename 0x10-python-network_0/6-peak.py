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
    list_copy = list_of_integers
    beg = 0
    end = len(list_copy)-1

    if list_copy[beg] > list_copy[beg+1]:
        return list_copy[beg]
    if list_copy[end] > list_copy[end-1]:
        return list_copy[end]

    mid = (beg+end)//2
    if list_copy[mid-1] < list_copy[mid] and list_copy[mid+1] < list_copy[mid]:
        return list_copy[mid]
    if list_copy[mid] < list_copy[mid-1]:
        return find_peak(list_copy[beg:mid+1])
    elif list_copy[mid] < list_copy[mid+1]:
        return find_peak(list_copy[mid:end+1])
    else:
        return list_copy[beg]
