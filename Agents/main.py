# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 23:48:50 2022

@author: Juan Sebastian Velasquez
"""

import readFile
import agents
import ia_algorithms

Test = 3

def transformData(width, height, lines):
    
    mainMaze = agents.Maze(width,height)
    
    for x in range(len(lines)):
        for y in range(len(lines)):
            if lines[x][y] == 2:
                cheese = agents.Cheese(x,y,mainMaze)
            if lines[x][y] == 3:
                mouse = agents.MouseAgent1(x,y,mainMaze)
            mainMaze.setElement(x, y, lines[x][y])
    
    return mouse, mainMaze, cheese

def main():

    width, height, lines = readFile.input(Test)
    mouse, mainMaze, cheese = transformData(width, height, lines)
    
    ia_algorithms.runIA(mouse, mainMaze, cheese)
        

main()


