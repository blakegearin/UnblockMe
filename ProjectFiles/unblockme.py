### Name: Blake Buthod, Ethan Brizendine, Thomas Goodman, & George Wood
### Date: 12-9-2016
### File unblockme.py
### Implements the unblock me style puzzle for state space search

from informedSearch import *
from block import *

class UnblockState(InformedProblemState):
    """
    The unblock me style puzzle: Given a 6x6 grid filled with blocks
    and having one exit, the goal is to get a particular block to the exit.
    Blocks can only move in the direction that they are oriented. In other
    words, vertical blocks can only move vertically, and horizontal
    blocks can only move horizontally.
    Each operator returns a new instance of this class representing
    the successor state.
    """
    def __init__(self, blockList):
        self.blockList = blockList
    def __str__(self):
        """
        Required method for use with the Search class.
        Returns a string representation of the state.
        """ 
    def illegal(self):
        """
        Required method for use with the Search class.
        Tests whether the state is illegal.
        """
    def equals(self, state):
        """
        Required method for use with the Search class.
        Determines whether the state instance and the given
        state are equal.
        """
    def moveUp(self):
        """
        """
    def moveDown(self):
        """
        """
    def moveLeft(self):
        """
        """

    def moveRight(self):
        """
        """

    ## A* dist search    
    def heuristic(self, goal):
    
    def operatorNames(self):
        """
        Required method for use with the Search class.
        Returns a list of the operator names in the
        same order as the applyOperators method.
        """
        return ["moveUp", "moveDown",
                "moveLeft", "moveRight"]
    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of possible successors to the current
        state, some of which may be illegal.  
        """
        return [self.moveUp(), self.moveDown(),
                self.moveLeft(), self.moveRight()]


# Gets problem state from input text file.
with open("unblockState.txt") as textFile:
    probState = [line.split() for line in textFile]

blockCount = 0
blockList = []

# Takes the input problem state and creates a list of block objects from it
for row in probState:
    for column in row:
        checkBlock = probState[row][column]
        # Checks if the current space is nonempty and, if so, if the
        # encountered block has not already been added to the list.
        if checkBlock != 0 and checkBlock > blockCount:
            # Checks if the new block is horizontal or vertical,
            # then if it is two or three spaces long, and finally
            # adds it to the list of blocks.
            if probState[row][column + 1] == checkBlock:
                if probState[row][column + 2] == checkBlock:
                    newBlock = Block(checkBlock, row, column, 3, "h")
                else:
                    newBlock = Block(checkBlock, row, column, 2, "h")
                
            elif probState[row + 1][column] == checkBlock:
                if probState[row + 2][column] == checkBlock:
                    newBlock = Block(checkBlock, row, column, 3, "v")
                else:
                    newBlock = Block(checkBlock, row, column, 2, "v")
            blockCount += 1
            blockList.append(newBlock)
                    
# Initiates the informed search towards the goal state
# GOAL STATE NEEDS FIXING
InformedSearch(UnblockState(tileList), UnblockState([[0,0,0,0,0,0],
                                                     [0,0,0,0,0,0],
                                                     [0,0,0,0,0,0],
                                                     [0,0,0,0,0,0],
                                                     [0,0,0,0,0,0],
                                                     [0,0,0,0,0,0]]))

