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
## freeRight():
##   True if the tile to the right is free (=no wall)
##
## freeLeft():
##   True if the tile to the left is free (=no wall)
##
## forward/left/right is always with respect to the orientation of the robot
##
## while(condition):
## 	code
##	code
##    As long as condition is True, execute the indented code
##
## if conditie1:
##	code1
##	code1
## elif conditie2:
## 	code2
## 	code2
## else:
## 	codea
## 	codea
##    Execute the lines with code1 if condition1 is True
##			     code2 if condition1 is False and condition2 is True
##                           code3 if both condition1 and condition2 are False
##########

from maze.maze import *

# Question 3: Solve maze3 using while and if - elif - else
loadMaze("maze/maze3a.txt")    

# You continue the code here




# The following instruction goes in the end
# It makes sure the window does not disappear after the program is finished
turtle.done()
        
