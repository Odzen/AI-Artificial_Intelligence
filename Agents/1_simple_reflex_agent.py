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
        except IndexError:
            pass
            
    
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
        self.foundCheese = False
    
    def previousPosition(self):
        return "The Mouse was here: ["+str(self.previousX)+" , " + str(self.previousY) +  "]"
        
    def __str__(self):
        return "The Mouse is here: ["+str(self.x)+" , " + str(self.y) +  "]"
    
    def hadfoundCheese(self):
        return self.foundCheese
    
    def isSomethingUp(self):
        if(self.maze.getElement(self.x-1, self.y) != 1):
            return False
        else:
            return True
    def isSomethingDown(self):
        if(self.maze.getElement(self.x+1, self.y) != 1):
            return False
        else:
            return True
    def isSomethingOnLeft(self):
        if(self.maze.getElement(self.x, self.y-1) != 1):
            return False
        else:
            return True
    def isSomethingOnRight(self):
        if(self.maze.getElement(self.x, self.y+1) != 1):
            return False
        else:
            return True
        
    def smellCheese(self):
        if(self.maze.getElement(self.x, self.y+1) == 2 or self.maze.getElement(self.x, self.y-1) == 2
           or self.maze.getElement(self.x+1, self.y) == 2 or self.maze.getElement(self.x-1, self.y) == 2):
            return True
        else:
            return False
    
    def moveLeft(self):
        try:
            if(not(self.isSomethingOnLeft())):
                if(self.maze.getElement(self.x, self.y-1) == 2):
                    self.foundCheese = True
                    print("Found Cheese, Congrats!!")
                self.maze.setElement(self.x, self.y-1, 3)
                self.maze.setElement(self.x, self.y, 0)
                self.previousX = self.x
                self.previousY = self.y
                self.y = self.y - 1
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
                self.previousX = self.x
                self.previousY = self.y
                self.x = self.x - 1
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
                self.previousX = self.x+1
                self.previousY = self.y
                self.x = self.x+1
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
                self.previousX = self.x
                self.previousY = self.y
                self.y = self.y + 1
                if(self.smellCheese()):
                    print("Cheese close!!")
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
    
    step = 0
    while(not(mouse.hadfoundCheese())):
        if((not (mouse.isSomethingOnLeft())) and (not (mouse.isSomethingUp())) and (not (mouse.isSomethingOnRight())) and (not(mouse.isSomethingDown()))):
            mouse.moveUp()
            step+=1
        if((not (mouse.isSomethingOnLeft())) and (not (mouse.isSomethingUp())) and (not (mouse.isSomethingOnRight())) and mouse.isSomethingDown()):
            mouse.moveUp()
            step+=1
        if((not (mouse.isSomethingOnLeft())) and (not (mouse.isSomethingUp())) and mouse.isSomethingOnRight() and (not(mouse.isSomethingDown()))):
            mouse.moveUp()
            step+=1
        if((not (mouse.isSomethingOnLeft())) and (not (mouse.isSomethingUp())) and mouse.isSomethingOnRight() and mouse.isSomethingDown()):
            mouse.moveLeft()
            step+=1
        if((not (mouse.isSomethingOnLeft())) and mouse.isSomethingUp() and (not(mouse.isSomethingOnRight())) and (not(mouse.isSomethingDown()))):
            mouse.moveLeft()
            step+=1
        if((not (mouse.isSomethingOnLeft())) and mouse.isSomethingUp() and (not(mouse.isSomethingOnRight()))and mouse.isSomethingDown()):
            mouse.moveRight()
            step+=1
        if((not (mouse.isSomethingOnLeft())) and mouse.isSomethingUp() and mouse.isSomethingOnRight() and (not(mouse.isSomethingDown()))):
            mouse.moveLeft()
            step+=1
        if((not (mouse.isSomethingOnLeft())) and mouse.isSomethingUp() and mouse.isSomethingOnRight() and mouse.isSomethingDown()):
            mouse.moveLeft()
            step+=1
        if(mouse.isSomethingOnLeft() and (not (mouse.isSomethingUp())) and (not(mouse.isSomethingOnRight())) and (not(mouse.isSomethingDown()))):
            mouse.moveUp()
            step+=1
        if(mouse.isSomethingOnLeft() and (not (mouse.isSomethingUp())) and (not(mouse.isSomethingOnRight())) and mouse.isSomethingDown()):
            mouse.moveRight()
            step+=1
        if(mouse.isSomethingOnLeft() and (not (mouse.isSomethingUp())) and mouse.isSomethingOnRight() and (not(mouse.isSomethingDown()))):
            mouse.moveDown()
            step+=1
        if(mouse.isSomethingOnLeft() and (not (mouse.isSomethingUp())) and mouse.isSomethingOnRight() and mouse.isSomethingDown()):
            mouse.moveUp()
            step+=1
        if(mouse.isSomethingOnLeft() and mouse.isSomethingUp() and (not(mouse.isSomethingOnRight())) and (not(mouse.isSomethingDown()))):
            mouse.moveRight()
            step+=1
        if(mouse.isSomethingOnLeft() and mouse.isSomethingUp() and (not(mouse.isSomethingOnRight())) and mouse.isSomethingDown()):
            mouse.moveRight()
            step+=1
        if(mouse.isSomethingOnLeft() and mouse.isSomethingUp() and mouse.isSomethingOnRight() and (not(mouse.isSomethingDown()))):
            mouse.moveDown()
            step+=1
            
        print("Step: ", step)
        print(mainMaze)
        
    
    



runSimpleIA()
        
    