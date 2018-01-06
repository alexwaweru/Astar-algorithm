#!/usr/bin/env python3

from A* import *
from movement import *


def calculate_directions():
    path = shortest_path()
    directions= []
    directions.append(1)
    current_cell = path[0]
    for i in range(len(path)):
        
        #If current_row - next_row = 1, turn upwards
        if current_cell[1] - path[i][1]==1:
            directions.append(1)
            
        #If current_col - next_col = -1, turn right
        if current_cell[0] - path[i][0]==-1
            directions.append(2)

        #If current_row - next_row = -1, turn downwards
        if current_cell[1] - path[i][1]==-1:
            directions.append(3)

        #If current_col - next_col = 1, turn left
        if current_cell[0] - path[i][0]==1: 
            directions.append(4)
            
        current_cell = path[i]
    return directions


''' This method takes in the a list of directions and returns a list of angles
    the robot is supposed to turn right to before moving straight for 45 centimeters'''
def calculate_angles(directions):

    # Initialize a list to store the angles
    angles = []

    # Set the current direction to the first value in the directions list
    current_direction = directions[0]

    # Loop through the list of directions to calculate the adjacent angles
    for i in range(len(directions)):
        angle = abs((directions[i] - current_direction)*45)
        angles.append(angle)
        current_direction = directions[i]
    return angles[1:]

def move():
    directions = calculate_directions()
    angles = calculate_angles(directions)
    for angle in angles:
        turn_right(angle)
        drive_straight(48)
                   
    
        
            
            
        
    
    
        
