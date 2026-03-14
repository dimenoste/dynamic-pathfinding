import numpy as np
import queue


# create coordinates matrix 
coords =  [(4, 10), (21, 10), (21, 1), (4, 1), 
           (16, 6), (9, 6),  (13, 9), (12, 9), 
           (20, 9), (5, 9), (1, 1), (24, 1), (7, 6), 
           (18, 6), (11, 6), (14, 6), (9, 10), 
           (16, 10), (5, 11), (20, 11)]

# snake
snake1 = ['0', '5,10:5,11:5,12']
snake2 = ['1', '10,3:10,4:10,5']

parts_coords_str = snake1[1].split(":")
print(parts_coords_str)

parts_coords = [tuple ( map (int, parts_coords_str[x].split(",") ) ) 
                for x in range(len(parts_coords_str)) ] 

print(parts_coords)


# width = 25
# height = 13
# # Unpack x and y coordinates
# x_coords, y_coords = zip(*coords)

# # Create coordinate grids using meshgrid
# xx, yy = np.meshgrid(x_coords, y_coords, indexing='xy')

# print("X grid:\n", xx)
# print("Y grid:\n", yy)


# grid = np.zeros((25,13), int)
# for x,y in coords:
#     grid[x][y] = 1


class Grid2d():
    def __init__(self, coords, height, width):
        self.width = width
        self.height = height
        self.grid = np.zeros((width, height), int)
        self.coords = coords
    
    def fill_grid(self, value):
        for x,y in self.coords:
            grid[x][y] = 1

def get_coords_input_parts(parts_coords_str):
    return [tuple ( map (int, parts_coords_str[x].split(",") ) ) 
                for x in range(len(parts_coords_str)) ]


class Snake():
    def __init__(self, snake_input):
        # snake_input = ['0', '5,10:5,11:5,12']
        self.body = get_coords_input_parts(snake_input[1].split(":"))
        self.id  = int(snake_input[0])
    
    def update_body(self, snake_input):
        self.body = get_coords_input_parts(snake_input[1].split(":"))
    
    def get_coords_parts(self, part_number=None):
        if part_number is not None and part_number <= len(self.body) and part_number >= 0:
            print("from class ", self.body[part_number])
            return  self.body[part_number]
        else:
            return self.body
        
    def get_head(self):
        return self.body[0]
    
    def get_tail(self):
        return self.body[-1]
    
snake_input = ['0', '5,10:5,11:5,12']
snake = Snake(snake_input)

print("coordinates of snake :", snake.body)
print("snake id :", snake.id)
print("coordinates of part at index 2 :", snake.get_coords_parts(2))
print("all body parts coordinates :", snake.get_coords_parts()) ## no number part passed as parameter => get the coordinates of all parts body
print("head   coord :", snake.get_head())
print("tail   coord :", snake.get_tail())

snake_input = ['0', '5,10:5,11:5,12:5,13'] ## snake ate a power source and grows
snake.update_body(snake_input)
print("new tail   coord", snake.get_tail())


#     def get_neighbors(self, current):
#         neighbors = []
#         x_curr, y_curr = current
#         if  ((0 > x_curr)  or (x > self.width)):
#             return 
#         elif ((0 > x_curr)  or (x > self.height)):
#             return
#         if (x_curr + 1 <= width):
#             coords.add((x_curr + 1 , y_curr))
#         if (x_curr - 1 >= 0):
#             coords.add((x_curr - 1 , y_curr))
#         if (y_curr + 1 <= height):
#             coords.add((x_curr, y_curr + 1))
#         if (y_curr - 1 >= 0):
#             coords.add((x_curr , y_curr - 1))
    


        
            

        

    

# print(grid)

# destination = (10, 12)
# start = (0,0)

# ## Breadth first search
# frontier = queue.Queue()
# frontier.put(start)
# reached = set()


# def get_neighbors(current, width, height):
#     coords_neighbors = []
#     x_curr, y_curr = current
#     if x_curr + 1 < width
#     return coords_neighbors



# while not frontier.empty():
#     current = frontier.get()
#     for next in neighbors(current):
#         if not next in reached:
#             frontier.put(next)
#             reached.add(next)

