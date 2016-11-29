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
        self.orientation = orientation
        if orientation == "v":
            self.coords = [(x,y),(x,y+1)]
            if size == 3:
                self.coords.append((x,y+2))
        elif orientation == "h":
            self.coords = [(x,y),(x+1,y)]
            if size == 3:
                self.coords.append((x+2,y))
            
        self.boardSize = 6
        self.collidedPieces = 0
    def __str__(self):
        """
        Returns a string representation of the block.
        """
    def possibleMove(self, dist, blockList):
        """
        Moves the block by an input distance in the plane of the
        block's orientation. Marks the state if a piece has crossed
        over another piece.
        """
        
        if self.orientation == "v":
            for block in blockList:
                if dist >= 0:
                    for n in range(dist):
                        for coords in self.getCoords():
                            if ((coords[0], coords[1] + n) in
                                block.getCoords()) and (block.getNum() !=
                                                       self.getNum()):
                                self.collidedPieces = 1
                else:
                    for n in range(0, dist, -1):
                        for coords in self.getCoords():
                            if ((coords[0], coords[1] +n) in
                                block.getCoords()) and (block.getNum() !=
                                                        self.getNum()):
                                self.collidedPieces = 1
                        
            self.y += dist
            
        elif self.orientation == "h":
            for block in blockList:
                if dist >= 0:
                    for n in range(dist):
                        for coords in self.getCoords():
                            if ((coords[0] + n, coords[1]) in
                            block.getCoords()) and (block.getNum() !=
                                                    self.getNum()):
                                self.collidedPieces = 1
                else:
                    for n in range(0, dist, -1):
                        for coords in self.getCoords():
                            if ((coords[0] + n, coords[1]) in
                            block.getCoords()) and(block.getNum() !=
                                                   self.getNum()):
                                self.collidedPieces = 1
        
            self.x += dist

    def getNum(self):
        """
        Returns the block's number designation. 1 means it's the target block.
        """
        return self.blockNum
    
    def getCoords(self):
        """
        Returns the x and y coordinates of the block.
        """
        print ("coords: " + str(self.coords))
        return self.coords

    def getSize(self):
        """
        Returns the size of the block.
        """
        return self.size

    def getOrientation(self):
        """
        Returns the orientation of the block.
        """
        return self.orientation

    
        
