#!/usr/bin/python3
""" Unlock boxes """


def canUnlockAll(boxes):
    """ Unlock boxes"""
    unlocked_boxes = set()
    for i, box in enumerate(boxes):
        if i not in unlocked_boxes:
            unlocked_boxes.add(i)
            
            # Check all keys in the current box
            for key in box:
                if key not in unlocked_boxes:
                    unlocked_boxes.add(key)
    
    return len(unlocked_boxes) == len(boxes)
