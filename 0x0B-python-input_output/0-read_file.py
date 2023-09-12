#!/usr/bin/python3
"""
Module 0-read_file

Contains function to read a file.
"""


def read_file(filename=""):
    """
    funtion to read and print contents of a file.

    Args:
        filename : file
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
