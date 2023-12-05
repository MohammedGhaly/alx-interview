#!/usr/bin/python3
'''Lockboxes problems'''


def canUnlockAll(boxes: list):
    '''kicks off recursion'''
    return recursive(boxes)


def recursive(boxes, visited=None, current_box=0):
    if visited is None:
        visited = set()

    # Mark the current box as visited
    visited.add(current_box)

    # Check if all boxes are visited
    if len(visited) == len(boxes):
        return True

    # Explore keys in the current box
    keys = boxes[current_box]
    for key in keys:
        if key < len(boxes) and key not in visited:
            # Recursively try to unlock the box with the key
            if recursive(boxes, visited, key):
                return True

    # If all keys are explored and no more boxes can be unlocked, return False
    return False
