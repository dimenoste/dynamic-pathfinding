from queue import Queue
import numpy as np


start = (1, 2)

frontier = Queue()
frontier.put(start)
came_from = dict()

came_from[start] = None

class graph():
    def __init__(self, rows, cols):
        self.cols = cols
        self.rows = rows
        self.grid =  np.zeros((self.width, self.height), int)

    def fill_grid(self):
        for i in range(rows):   
    row = []

    
    for j in range(col):
        row.append(int(input()))    # user input for rows
    matrix.append(row)
    def add_obstacle(self.grid):
        for i

    def neighbors(current):
        curr_x, curr_y = current
        return [(curr_x + 1, curr_y), (curr_x , curr_y + 1), 
                (curr_x - 1, curr_y), (curr_x , curr_y - 1)]
    
    def display(origin, goal):




while not frontier.empty():
    current = frontier.get()
    for next in graph.neighbors(current):
        if next not in came_from:
            frontier.put(next)
            came_from[next] = current