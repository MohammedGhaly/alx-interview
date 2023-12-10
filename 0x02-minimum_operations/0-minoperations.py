#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n):
    '''
    a function to count the minumum operation a string of n characters
    can be formed by only copying and pasting the current string in the
    text editor, or just pasting the string in the clipboard
    '''
    if n <= 1:
        return 0

    cur = 2
    clipboard = 1
    no_steps = 2

    while n > cur:
        if (n-cur) > 0 and (n-cur) % cur == 0:
            clipboard = cur
            cur += clipboard
            no_steps += 2
        else:
            cur += clipboard
            no_steps += 1

    return no_steps
