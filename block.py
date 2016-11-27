### Name: Blake Buthod, Ethan Brizendine, Thomas Goodman, & George Wood
### Date: 12-9-2016
### File tile.py
### The tile object that is manipulated in the unblock me style puzzle

class Block:
    """
    The basic play object of the puzzle. Can only move in the direction
    of its orientation. The x and y coordinates are the upper leftmost
    spaces of the block.
    """
    def __init__(self, blockNum, x, y, size, orientation):
        self.blockNum = blockNum
        self.x = x
        self.y = y
        self.size = size
        self.orientation = orientation
    def __str__(self):
        """
        Returns a string representation of the block.
        """
    def move(self, dist):
        """
        Moves the block by an input distance in the plane of the
        block's orientation.
        """
        if self.orientation == "v":
            self.y += dist
        elif self.orientation == "h"
            self.x += dist
    def getCoords(self):
        """
        Returns the x and y coordinates of the block.
        """
        return x,y
        
