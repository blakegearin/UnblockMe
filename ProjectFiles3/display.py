### Name: Blake Buthod, Ethan Brizendine, Thomas Goodman, & George Wood
### Date: 12-29-2016
### File display.py
### Manages displaying the game screen

from graphics import *

#Declare some constants
window_width = 643
window_height = 643
background_color = color_rgb(106, 74, 36)
border_color = color_rgb(163, 129, 55)
border_width = 21
block_unit = 100 #One block unit is 100 pixels (so a 2x1 block is 200x100 pixels)

class Display:
    """
    The basic play object of the puzzle. Can only move in the direction
    of its orientation. The x and y coordinates are the upper leftmost
    spaces of the block.
    """
    
    def __init__(self, blocks):
        #Build a list of block image objects
        self.blocks = blocks
        self.blockImages = []
        for i in range(len(blocks)):
            coords = self.blockCoordsToScreenCoords(blocks[i])
            self.blockImages.append( Image( Point(coords[0],coords[1]), blocks[i].getImageName() ) )
           

        self.window = GraphWin("Unblock Me", window_width, window_height)
        self.window.setBackground(background_color)
        
	# left border
        self.border_left = Rectangle(Point(0, 0), Point(border_width, window_height))
        self.border_left.setFill(border_color)
        self.border_left.setOutline(border_color)
        self.border_left.draw(self.window)
	# right border
        self.border_right = Rectangle(Point(window_width - border_width, 0), Point(window_width, window_height))
        self.border_right.setFill(border_color)
        self.border_right.setOutline(border_color)
        self.border_right.draw(self.window)
	# top border
        self.border_top = Rectangle(Point(0, 0), Point(window_width, border_width))
        self.border_top.setFill(border_color)
        self.border_top.setOutline(border_color)
        self.border_top.draw(self.window)
	# bottom border
        self.border_top = Rectangle(Point(0, window_height - border_width), Point(window_width, window_height))
        self.border_top.setFill(border_color)
        self.border_top.setOutline(border_color)
        self.border_top.draw(self.window)
        # goal zone
        self.goal_zone = Rectangle(Point(window_width - border_width, border_width + block_unit * 2), Point(window_width, border_width + block_unit * 3))
        self.goal_zone.setFill(background_color)
        self.goal_zone.setOutline(background_color)
        self.goal_zone.draw(self.window)

    def drawBlocks(self, newBlocks):
        """
        Draws/Redraws all of the blocks on the screen
        """
        for i in range(len(self.blockImages)):
            #Undraw images
            self.blockImages[i].undraw()
            #Get both the current and new coordinates to see if there was a change
            coordsOld = self.blockCoordsToScreenCoords(self.blocks[i])
            coordsNew = self.blockCoordsToScreenCoords(newBlocks[i])
            #Move the images based on the change in coordinates and draw them
            self.blockImages[i].move(coordsNew[0] - coordsOld[0], coordsNew[1] - coordsOld[1])
            self.blockImages[i].draw(self.window)
        #Update the blocks to the new blocks
        self.blocks = newBlocks
                
    def blockCoordsToScreenCoords(self, block):
        """
        Takes a block's top-left coordinates and converts that to screen corordinates (pixels)
        """
        newCoords = list(block.getCoords()[0]) #Grab only the first coordinate pair (the top-left corner)
        blockWidth = block.getWidth() * block_unit
        blockHeight = block.getHeight() * block_unit

        #Y position
        newCoords[1] = (border_width + 1) +(newCoords[1] * block_unit) + int(blockHeight/2)
        #X Position
        newCoords[0] = (border_width + 1) + (newCoords[0] * block_unit) + int(blockWidth/2)
        
        return newCoords

