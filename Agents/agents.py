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
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [ [0] * height for i in range(width)]
        self.OUT = 5
    
    def getNumCells(self):
        """
        Return the total number of cells in the maze.

        returns: an integer
        """
        return self.width * self.height
    
    def setElement(self, x, y, new_element):
        assert(type(x) == int and type(y) == int and type(new_element) == int)
        try:
            self.maze[x][y] = new_element
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
    
    # 5 is a case when is trying to access to a position outside from the maze
    def getElement(self, x, y):
        if(x < 0 or y < 0):
            result = self.OUT
        else:
            assert(type(x) == int and type(y) == int)
            result = 1
            try:
                result = self.maze[x][y]
            except IndexError as e:
                result = self.OUT
        return result
            
    
    def __str__(self):
        string = ""
        for x in range(self.width):
            for y in range(self.height):
                string+= str(self.maze[x][y]) + "| "
            string+="\n"
        return string
            

# Recieves a Maze and an initial position of the Mouse
class MouseAgent1(object):
    def __init__(self, x, y, maze):
        self.x = x
        self.y= y
        self.maze = maze
        maze.setElement(x,y,3)
        self.foundCheese = False
    
    def __str__(self):
        return "The Mouse is here: ["+str(self.x)+" , " + str(self.y) +  "]"
    
    def hadfoundCheese(self):
        return self.foundCheese
    
    def isSomethingUp(self):
        if(self.maze.getElement(self.x-1, self.y) == 1 or self.maze.getElement(self.x-1, self.y) == 5):
            return True
        else:
            return False
    def isSomethingDown(self):
        if(self.maze.getElement(self.x+1, self.y) ==1 or self.maze.getElement(self.x+1, self.y) == 5):
            return True
        else:
            return False
    def isSomethingOnLeft(self):
        if(self.maze.getElement(self.x, self.y-1) == 1 or self.maze.getElement(self.x, self.y-1) == 5):
            #print("If:",self.maze.getElement(self.x, self.y-1))
            return True
        else:
            #print("Else:",self.maze.getElement(self.x, self.y-1))
            return False
    def isSomethingOnRight(self):
        if(self.maze.getElement(self.x, self.y+1) == 1 or self.maze.getElement(self.x, self.y+1) == 5):
            return True
        else:
            return False
        
    def smellCheese(self):
        if(self.maze.getElement(self.x, self.y+1) == 2 or self.maze.getElement(self.x, self.y-1) == 2
           or self.maze.getElement(self.x+1, self.y) == 2 or self.maze.getElement(self.x-1, self.y) == 2):
            return True
        else:
            return False
    
    def setPosition(self,x, y):
        self.x = x
        self.y = y
        
    def moveLeft(self):
        try:
            if(not(self.isSomethingOnLeft())):
                if(self.maze.getElement(self.x, self.y-1) == 2):
                    self.foundCheese = True
                    print("Found Cheese, Congrats!!")
                self.maze.setElement(self.x, self.y-1, 3)
                self.maze.setElement(self.x, self.y, 0)
                self.setPosition(self.x, self.y-1)
                if(self.smellCheese()):
                    print("Cheese close!")
            else:
                print("Cannot move, something on the left")
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
    
    def moveUp(self):
        try:
            if(not (self.isSomethingUp())):
                if(self.maze.getElement(self.x-1, self.y) == 2):
                    self.foundCheese = True
                    print("Found Cheese, Congrats!!")
                self.maze.setElement(self.x-1, self.y, 3)
                self.maze.setElement(self.x, self.y, 0)
                self.setPosition(self.x-1, self.y)
                if(self.smellCheese()):
                    print("Cheese close!!")
            
            else:
                print("Cannot move, something Up")
                
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
            
    def moveDown(self):
        try:
            if(not(self.isSomethingDown())):
                if(self.maze.getElement(self.x+1, self.y) == 2):
                    self.foundCheese = True
                    print("Found Cheese, Congrats!!")
                self.maze.setElement(self.x+1, self.y, 3)
                self.maze.setElement(self.x, self.y, 0)
                self.setPosition(self.x+1, self.y)
                if(self.smellCheese()):
                    print("Cheese close!!")
            else:
                print("Cannot move, something Down")
                
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
            
    def moveRight(self):
        try:
            if(not(self.isSomethingOnRight())):
                if(self.maze.getElement(self.x, self.y+1) == 2):
                    self.foundCheese = True
                    print("Found Cheese, Congrats!!")
                self.maze.setElement(self.x, self.y+1, 3)
                self.maze.setElement(self.x, self.y, 0)
                self.setPosition(self.x, self.y+1)
                if(self.smellCheese()):
                    print("Cheese close!!")
            else:
                print("Cannot move, something on the Right")

        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
        

        
# Agent 1
class MouseAgent2(MouseAgent1):
    def __init__(self, x, y, maze):
        super().__init__(self, x, y, maze)
        self.previousX = x
        self.previousY = y
        self.previuosPositions = []
    
    def previousPosition(self):
        return "The Mouse was here: ["+str(self.previousX)+" , " + str(self.previousY) +  "]"
    
    def getPreviousPositions(self):
        return self.previuosPositions
    
    def setPreviousPositions(self, x, y):
        copy = self.previuosPositions[:]
        copy.append((x,y))
        self.previuosPositions = copy
    
    def visitedPosition(self, x, y):  
        point = (int(self.x), int(self.y))
        if point not in self.previuosPositions:
            self.previuosPositions.append(point)

    
    def hadVisitedPosition(self,x,y):
        if (x,y) not in self.previuosPositions:
            return True
        else:
            return False
    
    def moveLeft(self):
        if(not(self.hadVisitedPosition(self.x, self.y-1))):
            super().moveLeft()
        else:
            print("Left position visited in the previous move")

    def moveUp(self):
        if(not(self.hadVisitedPosition(self.x-1, self.y))):
            super().moveUp()
        else:
            print("Upper position visited in the previous move")

    def moveDown(self):
        if(not(self.hadVisitedPosition(self.x+1, self.y))):
            super().moveDown()
        else:
            print("Down position visited in the previous move")

    def moveRight(self):
        if(not(self.hadVisitedPosition(self.x, self.y+1))):
            super().moveRight()
        else:
            print("Right position visited in the previous movement")
    


# Recieves a Maze and an initial position of the Cheese
class Cheese(object):
    def __init__(self, x, y, maze):
        self.x = x
        self.y= y
        self.maze = maze
        maze.setElement(x,y,2)
        
    def __str__(self):
        return "The Cheese is here["+str(self.x)+" , " + str(self.y) +  "]"             
               

        
    