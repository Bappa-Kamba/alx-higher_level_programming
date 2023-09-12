#!/usr/bin/python3
"""
Module 100-append_after

Contains function that inserts a line of text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    appends str after lines that include keyword (search_string)
    """
    with open(filename, mode="r+", encoding="utf-8") as f:
        new_text = ""
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string
        f.seek(0)
        f.write(new_text)
