### Name: Blake Buthod
### Date: 9-30-2016
### File eightPuzzle.py
### Implements the eight puzzle for state space search

from informedSearch import *

class EightState(InformedProblemState):
    """
    The eight puzzle: Suppose that you are given a 3 by 3 grid
    with 8 numbered tiles and one blank space. The goal is to
    arrange the numbered tiles so that 1 is in the top left and
    moving clockwise around the grid each number is one greater
    than its predecessor.

    Each operator returns a new instance of this class representing
    the successor state.
    """
    def __init__(self, tiles):
        self.tiles = tiles
    def __str__(self):
        """
        Required method for use with the Search class.
        Returns a string representation of the state.
        """
        return "("+str(self.tiles)+")"    
    def illegal(self):
        """
        Required method for use with the Search class.
        Tests whether the state is illegal.
        """
        if type(self.tiles) is int: return 1
        for tile in self.tiles:
            if tile > 8 or tile < 0: return 1 
        if len(self.tiles) > 9: return 1
        return 0
    def equals(self, state):
        """
        Required method for use with the Search class.
        Determines whether the state instance and the given
        state are equal.
        """
        return self.tiles==state.tiles
    def moveUp(self):
        """
        Moves the blank tile up.
        """
        zeroTile = self.tiles.index(0)
        if zeroTile <= 2: return EightState(-1)
        if zeroTile >= 3 and zeroTile <= 8:
            destination = zeroTile-3
            newTiles = self.tiles[:]
            newTiles[zeroTile] = newTiles[destination]
            newTiles[destination] = 0
            return EightState(newTiles)
    def moveDown(self):
        """
        Moves the blank tile down.
        """
        zeroTile = self.tiles.index(0)
        if zeroTile >= 6: return EightState(-1)
        if zeroTile >= 0 and zeroTile <= 5:
            destination = zeroTile+3
            newTiles = self.tiles[:]
            newTiles[zeroTile] = newTiles[destination]
            newTiles[destination] = 0
            return EightState(newTiles)
    def moveLeft(self):
        """
        Moves the blank tile left.
        """
        zeroTile = self.tiles.index(0)
        if zeroTile==0 or zeroTile==3 or zeroTile==6: return EightState(-1)
        else:
            destination = zeroTile-1
            newTiles = self.tiles[:]
            newTiles[zeroTile] = newTiles[destination]
            newTiles[destination] = 0
            return EightState(newTiles)
    def moveRight(self):
        """
        Moves the blank tile right.
        """
        zeroTile = self.tiles.index(0)
        if zeroTile==2 or zeroTile==5 or zeroTile==8: return EightState(-1)
        else:
            destination = zeroTile+1
            newTiles = self.tiles[:]
            newTiles[zeroTile] = newTiles[destination]
            newTiles[destination] = 0
            return EightState(newTiles)
    ## BFS
##    def heuristic(self, goal):
##        return 0
    
    ## A* tile search
##    def heuristic(self, goal):
##        count = 0
##        for tile in self.tiles:
##            if self.tiles[tile] != goal.tiles[tile]:
##                count += 1
##        return count

    ## A* dist search    
    def heuristic(self, goal):
        count = 0
        for tile in self.tiles:
            thisTileAmount = self.tiles[tile]
            destination = goal.tiles.index(thisTileAmount)
            if tile+1 == destination or tile-1 == destination or tile+3 == destination or tile-3 == destination:
                count += 1
            elif tile+2 == destination or tile-2 == destination or tile+4 == destination or tile-4 == destination or tile+6 == destination or tile-6 == destination:
                count += 2
            elif tile+5 == destination or tile-5 == destination or tile+7 == destination or tile-7 == destination:
                count += 3  
            elif tile+8 == destination or tile-8 == destination:
                count += 4
        return count
    
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


InformedSearch(EightState([7,4,5,6,0,3,8,1,2]), EightState([1,2,3,8,0,4,7,6,5]))

##        Node Expansions
##Problem   BFS  A*(tiles)  A*(dist)     Data
##   A        7          3         3     [1,3,0,8,2,4,7,6,5]
##   B       91          8         7     [1,3,4,8,6,2,0,7,5]
##   C      156         19        10     [0,1,3,4,2,5,8,7,6]
##   D      690         48        30     [7,1,2,8,0,3,6,5,4]
##   E      856         48        30     [8,1,2,7,0,4,6,5,3]
##   F     1621        102        21     [2,6,3,4,0,5,1,8,7]
##   G     8361        337        56     [7,3,4,6,1,5,8,0,2]
##   H    50312       3529       208     [7,4,5,6,0,3,8,1,2]
