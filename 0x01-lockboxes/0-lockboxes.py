#!/usr/bin/python3
'''Lockboxes problems'''


def canUnlockAll(boxes: list):
    '''kicks off recursion'''
    if len(boxes) < 2:
        return True
    boxes_map = {i: i == 0 for i in range(len(boxes))}
    recursive(boxes, boxes_map, keys=boxes[0])
    return all(value for value in boxes_map.values())


def recursive(boxes, boxes_map: dict, keys):
    '''recursive function to unlock the box'''
    for key in keys:
        if 0 <= key < len(boxes) and not boxes_map[key]:
            boxes_map[key] = True
            recursive(boxes, boxes_map, boxes[key])
