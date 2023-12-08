#!/usr/bin/python3
'''Rotating 2D-Matrix'''


def rotate_2d_matrix(matrix: list):
    '''rotating 2d matrix in place'''

    # mapping the matrix to contain old and new values
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = {'old': matrix[i][j], 'new': 0}

    # rotating the matrix
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            matrix[i][-(j+1)]['new'] = matrix[j][i]['old']

    # mapping the matrix to its initial form
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = matrix[i][j]['new']
