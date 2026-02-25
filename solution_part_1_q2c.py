##########
## Use following functions to move in the maze:
## 
## goForward():
##   Move one tile forward
##
## turnRight():
##   Turn 45 degrees clockwise
##
## turnLeft():
##   Turn 45 degrees counter-clockwise
##
## freeForward():
##   look in front of the robot; True if the tile ahead is free (=no wall)
##
## forward/left/right is always with respect to the orientation of the robot
##
## while(condition):
## 	code
##	code
##    As long as condition is True, execute the indented code
##########

from maze.maze import *
loadMaze("maze/maze2c.txt")

# Question 2c: solve the maze with double while loop
# You continue the code here
while not foundExit():
  while (freeForward()):
    goForward()
  turnLeft()

# The following instruction goes in the end
# It makes sure the window does not disappear after the program is finished
turtle.done()
