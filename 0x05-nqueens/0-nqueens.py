#!/usr/bin/python3
"""N Queens"""
import sys


def solveNQueens(n: int):
    """kicks off recursion and formats the final result to be printed"""
    board = [[1 for y in range(n)] for x in range(n)]
    recursive(board)


def recursive(board, next_row=0):
    """recursive function to find valid boards"""
    if next_row == len(board):
        my_print_board(board)
        return

    for i in range(next_row, len(board)):
        if 1 not in board[i]:
            break
        for j in range(len(board)):
            if board[i][j] in [0, 2]:
                continue
            board[i][j] = 2
            recursive(exclude(board, i, j), i+1)
            board[i][j] = 1
        if 2 not in board[i]:
            break
    return


def exclude(b, i, j):
    """excludes invalid postions for the queens"""
    board = copy_board(b)

    right_diagonal_add = i + j
    left_diagonal_diff = i - j
    # exclude row
    for idx in range(len(board)):
        if board[i][idx] == 1:
            board[i][idx] = 0
    # exclude column
    for el in board:
        if el[j] == 1:
            el[j] = 0

    # exclude diagonals
    for row_index in range(len(board)):
        for col_index in range(len(board)):
            if board[row_index][col_index] == 1 \
                and (col_index + row_index == right_diagonal_add
                     or row_index - col_index == left_diagonal_diff):
                board[row_index][col_index] = 0

    return board


def copy_board(b):
    '''returns a copy of the board'''
    board = []
    for el in b:
        board.append(el.copy())
    return board


def my_print_board(board):
    """Print allocated positions to the queen"""
    b = []

    for i in range(len(board)):
        b.append([i, board[i].index(2)])
    print(b)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except BaseException:
    print("N must be a number")
    exit(1)

if (n < 4):
    print("N must be at least 4")
    exit(1)

solveNQueens(n)
