#!/usr/bin/python3
""" unlock boxes """

def canUnlockAll(boxes):
    """ Unlock boxes"""
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    
    for i in range(len(boxes)):
        for key in boxes[i]:
            if 0 <= key < len(boxes) and i != key:
                unlocked[key] = True
    
    return all(unlocked)
