# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 00:15:50 2022

@author: Juan Sebastian Velasquez Acevedo
"""

def runIA(mouse, mainMaze, cheese, maxSteps):
    """

    Parameters
    ----------
    mouse : Mouse (Could be any of the 4 agents)
        The Functions will behave differently depending on the type of mouse.
    mainMaze : Maze
    cheese : Cheese

    Returns void, just executes the fucntion and print the path
    -------

    """
    
    steps = 0
    while(not(mouse.hadfoundCheese()) and steps <= maxSteps):
        print("Step: ", steps)
        if((not (mouse.isSomethingOnLeft())) and (not (mouse.isSomethingUp())) and (not (mouse.isSomethingOnRight())) and (not(mouse.isSomethingDown()))):
            print("Caso - 1")
            mouse.moveUp()
            steps+=1
        if((not (mouse.isSomethingOnLeft())) and (not (mouse.isSomethingUp())) and (not (mouse.isSomethingOnRight())) and mouse.isSomethingDown()):
            print("Caso - 2")
            mouse.moveUp()
            steps+=1
        if((not (mouse.isSomethingOnLeft())) and (not (mouse.isSomethingUp())) and mouse.isSomethingOnRight() and (not(mouse.isSomethingDown()))):
            print("Caso - 3")
            mouse.moveUp()
            steps+=1
        if((not (mouse.isSomethingOnLeft())) and (not (mouse.isSomethingUp())) and mouse.isSomethingOnRight() and mouse.isSomethingDown()):
            print("Caso - 4")
            mouse.moveUp()
            steps+=1
        if((not (mouse.isSomethingOnLeft())) and mouse.isSomethingUp() and (not(mouse.isSomethingOnRight())) and (not(mouse.isSomethingDown()))):
            print("Caso - 5")
            mouse.moveLeft()
            steps+=1
        if((not (mouse.isSomethingOnLeft())) and mouse.isSomethingUp() and (not(mouse.isSomethingOnRight()))and mouse.isSomethingDown()):
            print("Caso - 6")
            mouse.moveRight()
            steps+=1
        if((not (mouse.isSomethingOnLeft())) and mouse.isSomethingUp() and mouse.isSomethingOnRight() and (not(mouse.isSomethingDown()))):
            print("Caso - 7")
            mouse.moveLeft()
            steps+=1
        if((not (mouse.isSomethingOnLeft())) and mouse.isSomethingUp() and mouse.isSomethingOnRight() and mouse.isSomethingDown()):
            print("Caso - 8")
            mouse.moveLeft()
            steps+=1
        if(mouse.isSomethingOnLeft() and (not (mouse.isSomethingUp())) and (not(mouse.isSomethingOnRight())) and (not(mouse.isSomethingDown()))):
            print("Caso - 9")
            mouse.moveUp()
            steps+=1
        if(mouse.isSomethingOnLeft() and (not (mouse.isSomethingUp())) and (not(mouse.isSomethingOnRight())) and mouse.isSomethingDown()):
            print("Caso - 10")
            mouse.moveRight()
            steps+=1
        if(mouse.isSomethingOnLeft() and (not (mouse.isSomethingUp())) and mouse.isSomethingOnRight() and (not(mouse.isSomethingDown()))):
            print("Caso - 11")
            mouse.moveDown()
            steps+=1
        if(mouse.isSomethingOnLeft() and (not (mouse.isSomethingUp())) and mouse.isSomethingOnRight() and mouse.isSomethingDown()):
            print("Caso - 12")
            mouse.moveUp()
            steps+=1
        if(mouse.isSomethingOnLeft() and mouse.isSomethingUp() and (not(mouse.isSomethingOnRight())) and (not(mouse.isSomethingDown()))):
            print("Caso - 13")
            mouse.moveRight()
            steps+=1
        if(mouse.isSomethingOnLeft() and mouse.isSomethingUp() and (not(mouse.isSomethingOnRight())) and mouse.isSomethingDown()):
            print("Caso - 14")
            mouse.moveRight()
            steps+=1
        if(mouse.isSomethingOnLeft() and mouse.isSomethingUp() and mouse.isSomethingOnRight() and (not(mouse.isSomethingDown()))):
            print("Caso - 15")
            mouse.moveDown()
            steps+=1
        
        print(mainMaze)

## Solutions by hand for testing

"""
#Solution Maze 1
mouse.moveUp()
print(mainMaze)
#print(mouse.getPreviousPositions())
    
mouse.moveLeft()
print(mainMaze)
#print(mouse.getPreviousPositions())


mouse.moveUp()
print(mainMaze)
#print(mouse.getPreviousPositions())


mouse.moveUp()
print(mainMaze)
print(mouse.getPreviousPositions())


mouse.moveLeft()
print(mainMaze)
print(mouse.getPreviousPositions())

mouse.moveLeft()
print(mainMaze)
#print(mouse.previousPosition())
print(mouse.getPreviousPositions())

mouse.moveRight()
print(mainMaze)
"""

"""
#Solution Maze 2

print(mainMaze)
#print(not(mouse.isSomethingDown()))
# Case 11 - Correct
#print(mouse.isSomethingOnLeft() and (not (mouse.isSomethingUp())) and mouse.isSomethingOnRight() and (not(mouse.isSomethingDown())))


mouse.moveDown()
print(mainMaze)


mouse.moveRight()
print(mainMaze)


mouse.moveRight()
print(mainMaze)


mouse.moveUp()
print(mainMaze)


mouse.moveRight()
print(mainMaze)


mouse.moveUp()
print(mainMaze)
print(mouse.hadfoundCheese())
#print(mouse.getPreviousPositions())
    
"""

