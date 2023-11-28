#!/usr/bin/python3
"""a module that contains pascal_triangle function"""


def pascal_triangle(n):
    """
    a function that returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    triangle = pascal_triangle(n-1)
    last_row = triangle[-1]
    new_row = [1]
    for i in range(1, len(last_row)):
        new_row.append(last_row[i] + last_row[i-1])
    new_row.append(1)
    triangle.append(new_row)
    return triangle
