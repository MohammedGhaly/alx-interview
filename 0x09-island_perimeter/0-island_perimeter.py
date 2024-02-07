#!/usr/bin/python3
"""island perimeter problem"""


def island_perimeter(grid):
    '''
    a function that calculates the perimeter of an island
    where 1 and 0 represent land and water respectively
    '''
    perimeter = 0
    for row, row_value in enumerate(grid):
        for col, value in enumerate(row_value):

            if value:
                top = (grid[row-1][col] == 0) if row > 0 else 1
                bottom = grid[row+1][col] == 0 if row < len(grid)-1 else 1
                left = grid[row][col-1] == 0 if col > 0 else 1
                right = grid[row][col +
                                  1] == 0 if col < len(row_value)-1 else 1
                perimeter += sum([top, bottom, right, left])
    return perimeter
