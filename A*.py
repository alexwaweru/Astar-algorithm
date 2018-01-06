#!/usr/bin/env python3

''' @author: Alex Njoroge Waweru'''
''' This an implementation of the A* Algorithmns for path finding.
    An adjacency grid (list of lists) is used to represent the traversal environment.'''

from queue import *
from planning_map import * 

'''This method takes in a node and returns its 4 point connectivity neighbours'''
def get_neighbors(node):

    # Get all rows and columns adjacent to the current row, current row and current col inclusive
    # Check if rows and columns are within the grid (traversal environment)
    # Create a list of cells using the remaining row and cols combinations
    # Remove the current cell from the list
    # Remove all corner cells from the list (ensures 4 point connectivity)
    
    neighbours = []
    rows = [node[1]-1, node[1], node[1]+1] # All adjacent rows including current row
    cols = [node[0]-1, node[0], node[0]+1] # All adjacent columns including current column
    
    # Combining rows and cols to get all possible neighbouring cells 
    for row in rows:
        # Check if the row is within the traversal environment
        if (row < total_rows and row >= 0): 
            for col in cols:
                # Check if the column is within the traversal environment
                if (col < total_cols and col >= 0):
                    # Remove corner cells to ensure 4 point connectivity
                    # To use 8-point connectivity remove this condition
                    if ((row!=node[1]-1 and row!=node[1]+1) or (col!=node[0]-1 and col!=node[0]+1)):
                        neighbour = (col,row)
                        # Remove the current cell from the neighbours 
                        if (neighbour!= (node[0], node[1])): 
                            if grid[neighbour[1]][neighbour[0]] != 1: #grid is imported from the planning_map
                                neighbours.append(neighbour)
    return neighbours


''' This method takes in a goal and node and returns the estimated cost from the node to the goal'''
def heuristic(goal, next_node):    

    # The heuristic cost is the sum of the row distance and the column distance
    (goal_row, goal_col) = goal
    (next_node_row, next_node_col) = next_node
    return abs(goal_row - next_node_row) + abs(goal_col - next_node_col)


''' This method sets the value of the goal node on the adjacency grid to 2'''
def set_goal():

    # The goal value is set to 2
    row = goal[1]
    col = goal[0]
    grid[row][col] = 2
    

''' This methods takes in the current_node and the next_node and returns the traversal cost'''
def cost(current, next):
    
    # Get the row and col so as to map to the grid map
    row = next[1]
    col = next[0]
    cell_traversal_cost = grid[row][col]
    if  cell_traversal_cost == 0: # The cell holds 0 on the grid meaning it is traversable and its default traversal cost is 1
        #In this case assume the traversal cost is 1 and is uniform across all neighbours
        return 1
    else: # In this case it maybe a mountain (6) or hill(3) or blocked road (8) and its traversal is set to a higher value
        return cell_traversal_cost 
        


''' This method takes in the adjaceny grid (graph), the start node and the end node and
    returns a map with nodes as keys and their predecessor as vale, and a map of nodes as key
    and g-value as value'''
def Astar_search(start, goal):
    
    # Create a priorityQueue
    priority_queue = PriorityQueue() # priorityQueue is imported from python's generic queue module

    # Put start node in the queue with priority 0 (0 represents its f=(g(s)+h(s)) value)
    priority_queue.put(start, 0)

    # Create a map to store predecessor of each traversed node ( node -> predecessor)
    predecessor = {}

    # Create a map to store cost_so_far of each traversed node ( node -> cost_so_far)
    cost_from_start = {}

    # Put the start node in the predecessor map with none as its value ( start -> none)
    predecessor[start] = None

    # Put the start node in the cost_from_start map with 0 as its value ( start -> 0)
    cost_from_start[start] = 0

    # While the priority_queue is not epmpty, set the node with the highest priority as the current_node
    while not priority_queue.empty():
       current_node = priority_queue.get()

       # When we get to the goal node break the loop
       if current_node == goal: # goal is imported from the planning_map 
          break
        
       # Get the neighbours of the current_node
       for next_node in get_neighbors(current_node):

          # For each neighbour node,
          # calculate its new_cost as the sum of the current_node's cost and the traversal cost between the current node and the neighbour node
          # g(s) = g(s') + cost(s', s)
          new_cost = cost_from_start[current_node] + cost(current_node, next_node)

          # If a neighbour node is not in the cost_from_start map, or its new cost is lower than the cost it has in the cost_from_start map
          # add it to the cost_from_start map with its new cost
          if next_node not in cost_from_start or new_cost < cost_from_start[next_node]:
             cost_from_start[next_node] = new_cost

             # Calculate a each neighbour node's priority (f(s) = g(s) + h(s)
             priority = new_cost + heuristic(goal, next_node) # goal is imported from planning_map

             # Add the neighbour node into the priority queue with its calculate priority
             priority_queue.put(next_node, priority)

             # Add the neighbour node into the predecessor map with current code as its value
             predecessor[next_node] = current_node
             
    return predecessor


''' This method takes in predecessor map, start node and goal node and returns a list of nodes representing the shortest path'''
def construct_optimal_path(predecessor, start, goal):

    # set the goal as the current_node
    current_node = goal # goal is imported from the planning_map

    # create a shortest_path list
    optimal_path = []

    # starting from the current_node, append predecessor values for each node to the optimal_path until you get to the node before the start node
    while current_node != start:
        optimal_path.append(current_node)
        current_node = predecessor[current_node]

    # Append the start node to the shortest_path to make it complete 
    optimal_path.append(start) 

    # The current path is ordered from the goal to the start node.
    # Reverse the path to reorder the nodes from the start to the goal
    optimal_path.reverse()
    
    return optimal_path


''' This method calls thee Astart_search method to get the predecessors and then goals the construct_optimal_path method
    get the optimal path from the start to the goal of the adjacency grid'''
def shortest_path():
    
    # Call the Astar_search to get a tuple of predecessors
    predecessors = Astar_search(start, goal)

    # Call the construct_optimal_path using the predecessors, start and goal to get the shortest path
    path = construct_optimal_path(predecessors, start, goal)
    return path

print(shortest_path())

    
