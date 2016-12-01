### Name: Blake Buthod, Ethan Brizendine, Thomas Goodman, & George Wood
### Date: 12-9-2016
### File tile.py
### The tile object that is manipulated in the unblock me style puzzle

from display import *

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

        #Get the file name for the image
        self.imageName = "images/"
        if size == 3:
             self.imageName += "3"
        elif size == 2:
             self.imageName += "2"
        
        if orientation == "v":
            self.coords = [(x,y),(x,y+1)]
            if size == 3:
                self.coords.append((x,y+2))
            #Add to imageName
            self.imageName += "_vert"
        elif orientation == "h":
            self.coords = [(x,y),(x+1,y)]
            if size == 3:
                self.coords.append((x+2,y))
            #Add to imageName
            self.imageName += "_hor"

         #Check if this is the red block for the image name
        if blockNum == 1:
            self.imageName += "_red"
        #Add the file extension for the image name
        self.imageName += ".png"
            
        self.boardSize = 6
        self.collidedPieces = 0

    def __str__(self):
        """
        Returns a string representation of the block.
        """
        return (str(self.blockNum) + " " + str(self.coords))
    def setCoords(self):

        self.coords[0] = (self.x, self.y)
        if self.orientation == "v":
            self.coords[1] = (self.x,self.y+1)
            if self.size == 3:
                self.coords[2] = (self.x,self.y+2)
        elif self.orientation == "h":
            self.coords[1] = (self.x+1, self.y)
            if self.size == 3:
                self.coords[2] = (self.x+2, self.y)
                
    def copy(self):
        return Block(self.blockNum, self.x, self.y,
                     self.size, self.orientation)
        
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
            self.setCoords()
            
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
            self.setCoords()

    def getNum(self):
        """
        Returns the block's number designation. 1 means it's the target block.
        """
        return self.blockNum
    
    def getCoords(self):
        """
        Returns the x and y coordinates of the block.
        """
        
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

    def getImageName(self):
        """
        Returns the image name string used by the block.  This is the file path to the image.
        """
        return self.imageName

    def getWidth(self):
        """
        Returns the width of the block.
        """
        width = 1
        if self.orientation == "h":
            width = self.size
        return width
    
    def getHeight(self):
        """
        Returns the height of the block.
        """
        height = 1
        if self.orientation == "v":
            height = self.size
        return height
        
