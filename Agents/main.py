# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 23:48:50 2022

@author: Juan Sebastian Velasquez
"""

import readFile
import agents
import ia_algorithms
# import signal
import time

Test = 2
MaxSteps = 15



def transformData(width, height, lines):
    
    mainMaze = agents.Maze(width,height)
    
    for x in range(len(lines)):
        for y in range(len(lines)):
            if lines[x][y] == 2:
                cheese = agents.Cheese(x,y,mainMaze)
            if lines[x][y] == 3:
                mouse = agents.MouseAgent2(x,y,mainMaze)
            mainMaze.setElement(x, y, lines[x][y])
    
    return mouse, mainMaze, cheese

def main():

    width, height, lines = readFile.input(Test)
    mouse, mainMaze, cheese = transformData(width, height, lines)
    ia_algorithms.runIA(mouse, mainMaze, cheese, MaxSteps)
    
    """
    It seems signal doesn't work in windows'
    
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(10)   # Ten seconds
    try:
        ia_algorithms.runIA(mouse, mainMaze, cheese)
    except Exception as e:
        print("Timed out!")
    """

        
"""
def signal_handler(signum, frame):
    raise Exception("Timed out!")
"""

    
main()

