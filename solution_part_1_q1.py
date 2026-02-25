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
##########

from maze.maze import *
loadMaze("maze/maze1.txt")

# Problem 1: Go to the target tile
turnRight()
goForward()
turnLeft()
goForward()
goForward()
turnRight()
goForward()
goForward()
turnLeft()
goForward()
goForward()
turnLeft()
goForward()
goForward()
goForward()


# You continue the code here




# The following instruction goes in the end
# It makes sure the window does not disappear after the program is finished
turtle.done()






