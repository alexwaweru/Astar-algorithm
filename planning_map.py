#!/usr/bin/env python3

'''@author: Alex Njoroge Waweru'''


total_cols = 8
total_rows = 6
traversibe = 0
obstacle = 1

''' An adjancency list representing a robot's known traversal environment'''
''' In real world the distance from each node is 45 centimeters'''

grid =           [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1, 1, 0, 0],
		  [0, 0, 1, 0, 0, 0, 1, 0],
                  [0, 0, 1, 0, 0, 0, 1, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0]]
		 

start = (4, 5)  # tuple of 2 values (c,r)
goal = (4, 0)   # tuple of 2 values (c,r)
