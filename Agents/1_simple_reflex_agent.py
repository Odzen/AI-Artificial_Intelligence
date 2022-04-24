# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 23:13:36 2022

@author: Juan Sebastian Velasquez Acevedo
"""

# Creat only the maze with  initially in each position
# 0 represents an open path
# 1 represents an obstacle
# 2 represents an object Cheese
# 3 represents an object Mouse
class Maze(object):
    def __init__(self, size):
        self.size = size
        self.maze = [[0] * size for i in range(size)]
    
    def getSize(self):
        return self.size
    
    def setElement(self, x, y, new_element):
        assert(type(x) == int and type(y) == int and type(new_element) == int)
        try:
            self.maze[x][y] = new_element
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
    
    def getElement(self, x, y):
        assert(type(x) == int and type(y) == int)
        try:
            return self.maze[x][y]
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
    
    def __str__(self):
        string = ""
        for x in range(self.size):
            for y in range(self.size):
                string+= str(self.maze[x][y]) + "| "
            string+="\n"
        return string
            

# Recieves a Maze and an initial position of the Mouse
class Mouse(object):
    def __init__(self, x, y, maze):
        self.x = x
        self.y= y
        self.maze = maze
        self.previousX = 0
        self.previousY = 0
        maze.setElement(x,y,3)
    
    def previousPosition(self):
        return "The Mouse was here: ["+str(self.previousX)+" , " + str(self.previousY) +  "]"
        
    def __str__(self):
        return "The Mouse is here: ["+str(self.x)+" , " + str(self.y) +  "]"
    
    def moveLeft(self):
        try:
            if(self.maze.getElement(self.x, self.y-1) != 1 and self.maze.getElement(self.x, self.y-1) != 2):
                self.maze.setElement(self.x, self.y-1, 3)
                self.maze.setElement(self.x, self.y, 0)
                self.previousX = self.x
                self.previousY = self.y
                self.y = self.y - 1
            else:
                print("Cannot move, something on the left")
                
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
    
    def moveUp(self):
        try:
            if(self.maze.getElement(self.x-1, self.y) != 1 and self.maze.getElement(self.x-1, self.y) != 2):
                self.maze.setElement(self.x-1, self.y, 3)
                self.maze.setElement(self.x, self.y, 0)
                self.previousX = self.x
                self.previousY = self.y
                self.x = self.x - 1
            
            else:
                print("Cannot move, something Up")
                
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
            
    def moveDown(self):
        try:
            if(self.maze.getElement(self.x+1, self.y) != 1 and self.maze.getElement(self.x+1, self.y) != 2):
                self.maze.setElement(self.x+1, self.y, 3)
                self.maze.setElement(self.x, self.y, 0)
                self.previousX = self.x+1
                self.previousY = self.y
                self.x = self.x+1 
            else:
                print("Cannot move, something Down")
                
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
            
    def moveRight(self):
        try:
            if(self.maze.getElement(self.x, self.y+1) != 1 and self.maze.getElement(self.x, self.y+1) != 2):
                self.maze.setElement(self.x, self.y+1, 3)
                self.maze.setElement(self.x, self.y, 0)
                self.previousX = self.x
                self.previousY = self.y
                self.y = self.y + 1
            else:
                print("Cannot move, something on the Right")
                
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
    

# Recieves a Maze and an initial position of the Cheese
class Cheese(object):
    def __init__(self, x, y, maze):
        self.x = x
        self.y= y
        self.maze = maze
        maze.setElement(x,y,2)
        
    def __str__(self):
        return "The Cheese is here["+str(self.x)+" , " + str(self.y) +  "]"

               
               
def runSimpleIA():    
    mainMaze = Maze(4)
    mouse = Mouse(3,3,mainMaze)
    cheese = Cheese(2,0,mainMaze)
    
    # Obstacles
    mainMaze.setElement(1, 0, 1)
    mainMaze.setElement(1, 3, 1)
    mainMaze.setElement(3, 2, 1)
    
    print(mainMaze)

    mouse.moveUp()
    mouse.moveLeft()
    
    print(mainMaze)
    mainMaze.setElement(1,2, 6)


runSimpleIA()
        
    