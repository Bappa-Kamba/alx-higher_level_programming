#!/usr/bin/python3
"""
Module 12-pascal_triangle

Contains functions to generate and print the Pascal's triangle
of height `n`.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the
    Pascal's triangle of n;
    empty list if n <= 0.
    """
    if n == 0:
        return [[]]
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for i in range(n - 1):
        triangle.append([a + b for a, b
                        in zip([0] + triangle[-1], triangle[-1] + [0])
                         ])
    return triangle
