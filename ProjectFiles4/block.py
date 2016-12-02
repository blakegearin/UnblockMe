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
        x = self.x
        y = self.y
        size = self.size
                
        if self.orientation == "v":
            ## Moving down
            if dist > 0:
                ## Checks to make sure not touching bottom
                if (size == 2 and y != 4) or (size == 3 and y != 3):
                    ## Cycles through every block on board
                    for block in blockList:
                        ## Eliminates itself if encountered
                        if block.getNum() != self.getNum():
                            ## Cycles through every coordinate of each block
                            for coords in block.getCoords():
                                ## Cycles through current top space to
                                ##    proposed new bottom space
                                for n in range(y, y + dist + (size - 1)):
                                    ## Checks that no two coordinates are equal
                                    if (coords == (x,n)):
                                        self.collidedPieces = 1
            ## Moving up, checks to make sure not on top row
            elif dist < 0 and y != 0:
                ## Cycles through every block on board
                for block in blockList:
                    ## Eliminates itself if encountered
                    if block.getNum() != self.getNum():
                        ## Cycles through every coordinate of each block
                        for coords in block.getCoords():
                            ## Cycles through proposed new top space
                            ##    to current bottom space
                            for n in range(y + dist, y + (size-1)):
                                ## Checks that no two coordinates are equal
                                if (coords == (x,n)):
                                    ## If equal, set collided
                                    self.collidedPieces = 1

##            if self.collidedPieces == 0 and dist != 0:
            self.y += dist
            self.setCoords()
            
        elif self.orientation == "h":
            ## Moving rightward
            if dist > 0:
                ## Checks to make sure not on right-most column
                if (size == 2 and x != 4) or (size == 3 and x != 3):
                    ## Cycles through every block on board
                    for block in blockList:
                        ## Eliminates itself if encountered
                        if block.getNum() != self.getNum():
                            ## Cycles through every coordinate of each block
                            for coords in block.getCoords():
                                ## Cycles through current left-most space
                                ##    to proposed new right-most space
                                for n in range(x, x + dist + (size-1)):
                                    ## Checks that no two coordinates are equal
                                    if (coords == (n,y)):
                                        ## If equal, set collided
                                        self.collidedPieces = 1
            ## Moving leftward, checks to make sure not on left-most column
            elif dist < 0 and x != 0:
                ## Cycles through every block on board
                for block in blockList:
                    ## Eliminates itself if encountered
                    if block.getNum() != self.getNum():
                        ## Cycles through every coordinate of each block
                        for coords in block.getCoords():
                            ## Cycles through proposed new left-most space
                            ##    to current right-most space
                            for n in range(x + dist, x + (size-1)):
                                ## Checks that no two coordinates are equal
                                if (coords == (n,y)):
                                    ## If equal, set collided
                                    self.collidedPieces = 1
                
##            if self.collidedPieces == 0 and dist != 0:
            self.x += dist
            self.setCoords()

    def moveBlock(self, xAmount, yAmount):
        self.x += xAmount
        self.y += yAmount
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

    def getCollided(self):
        """
        Returns the state of collision.
        """
        return self.collidedPieces
