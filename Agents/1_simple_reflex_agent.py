# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 23:13:36 2022

@author: Juan Sebastian Velasquez Acevedo
"""



#class Simple_Agent(object):
#   def __init__(self, maze, ):
    

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
            
            
    
    
"""
# Recieves a Maze and an initial position of the mouse
class Mouse(object):
    def __init__(self, x, y, maze):
        self.x = x
        self.y= y
        self.maze = maze
        
    def __str__(self):
        return "["+str(x)+" , " + str(y) +  "]"
               
    """

mainMaze = Maze(2)
print(mainMaze)
mainMaze.setElement(0, 1, 3)
print(mainMaze)
print(mainMaze.getElement(0, 0))