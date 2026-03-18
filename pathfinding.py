from queue import Queue
import numpy as np
import sys
from typing_extensions import TypeVarTuple, Unpack

MARKER_GOAL = "G"
MARKER_START = "S"
MARKER_OBSTACLE = "X"


class Grid:
    def __init__(self, cols: int, rows: int):
        self.cols = cols
        self.rows = rows
        self.grid = self.create_grid()

    def create_grid(self) -> np.ndarray:
        grid = np.zeros((self.cols, self.rows), dtype=object)
        return grid

    def add_start_dest(
        self,
        start: tuple[int, int],
        dest: tuple[int, int],
        obstacles: set[tuple[int, int]],
    ) -> np.ndarray | None:
        if not self.is_in_grid(start):
            print("start point not compatible with grid dimensions")
            return None
        if not self.is_in_grid(dest):
            print("destination point not compatible with grid dimensions")
            return None
        x_start, y_start = start
        x_goal, y_goal = dest
        self.grid[y_start][x_start] = MARKER_START
        self.grid[y_goal][x_goal] = MARKER_GOAL
        return self.grid

    def add_obstacles_to_grid(self, obstacles: set[tuple[int, int]]) -> np.ndarray:
        for point in obstacles:
            if self.is_in_grid(point):
                x, y = point
                self.grid[y][x] = MARKER_OBSTACLE
        return self.grid

    def is_in_grid(self, current: tuple[int, int]) -> bool:
        y_min = 0
        x_min = 0
        y_max = self.rows - 1
        x_max = self.cols - 1
        return (x_min <= current[1] <= x_max) and (y_min <= current[0] <= y_max)

    # def add_points(a :tuple[int,int], b : tuple[int,int]) -> tuple[int,int]:
    #     return (a[0]+b[0], a[1]+b[1])

    def display(self) -> None:
        for col in range(self.cols):
            for row in range(self.rows):
                print(self.grid[col][row], end=" ")
            print()


class Maze:
    parents = dict()

    def __init__(
        self,
        grid: Grid,
        obstacles: set[tuple[int, int]],
        start: tuple[int, int],
        destination: tuple[int, int],
    ):
        self.grid = grid
        self.obstacles = obstacles
        self.start = start
        self.destination = destination

    def build_maze(self, grid):
        self.grid = grid.add_start_dest(start = self.start, dest = self.destination)
        self.grid = grid.add_obstacles_to_grid(obstacles  = self.obstacles)


    def get_parents(
        self,
        curr: tuple[int, int],
        parents: dict[tuple[int, int], tuple[int, int] | None],
    ) -> set[tuple[int, int]] | None:
        cases_in_path = set()
        if curr != self.goal:
            print("make sure current case you are in is your final goal")
            return cases_in_path
        while curr != None:
            cases_in_path.add(curr)
            curr = parents[curr]
        return cases_in_path

    def get_neighbors(self, current: tuple[int, int]) -> set[tuple[int, int]] | None:
        neighbors = set()
        x, y = current
        left = (x - 1, y)
        right = (x + 1, y)
        down = (x, y + 1)
        up = (x, y - 1)

        if not self.is_in_grid(current):
            return None
        if self.grid.is_in_grid(left):
            neighbors.add(left)
        if self.grid.is_in_grid(right):
            neighbors.add(right)
        if self.grid.is_in_grid(up):
            neighbors.add(up)
        if self.grid.is_in_grid(down):
            neighbors.add(down)
        return neighbors

    def display_path(self, path: set[tuple[int, int]] | None) -> None:
        if not path:
            return
        for case in path:
            x, y = case
            if not (case == self.start or case == self.goal):
                self.grid[y][x] = "p"
        self.display()

    def solve_bfs(self):

        ## cases already visited
        is_visited = set()
        is_visited.add(self.start)
        ## cases to be visited
        to_visit_queue: Queue = Queue()
        to_visit_queue.put(self.start)
        ## parents of each case
        parents = dict()
        parents[self.start] = None
        curr = self.start

        while not (to_visit_queue.empty()):
            if curr == self.goal:
                print("goal found")
                break
            # get_neighbors
            neighbors = self.grid.get_neighbors(curr)
            for case in neighbors:
                # a case wiuld be the new current only if it has not been already visited
                if not (case in is_visited or case in self.obstacles):
                    to_visit_queue.put(case)
                    if not case in parents.keys():
                        parents[case] = curr
                    is_visited.add(case)
                    curr = case
            curr = to_visit_queue.get()

        path = self.get_parents(curr, parents)
        return path


# def get_parents(curr : tuple[int, int], goal : tuple[int, int], parents : dict[tuple[int,int], tuple[int, int] | None]) -> set[tuple[int, int]] | None:
#     cases_in_path = set()
#     if curr != goal:
#         print("make sure current case you are in is your final goal")
#         return cases_in_path

#     while curr != None:
#         cases_in_path.add(curr)
#         curr = parents[curr]

#     return cases_in_path


# def compute_path_bfs(start : tuple[int, int], goal : tuple[int, int], grid : Grid) -> set[tuple[int,int]]| None:
#     ## cases already visited
#     is_visited = set()
#     is_visited.add(start)

#     ## cases to be visited
#     to_visit_queue: Queue = Queue()
#     to_visit_queue.put(start)

#     ## parents of each case
#     parents = dict()
#     parents[start] = None

#     curr = start

#     while not (to_visit_queue.empty()):
#         if curr == goal:
#             print("goal found")
#             break
#         # get_neighbors
#         neighbors = grid.get_neighbors(curr)
#         for case in neighbors :
#             if not (case in is_visited or case in obstacles):
#                 to_visit_queue.put(case)
#                 if not case in parents.keys():
#                     parents[case] = curr
#                 is_visited.add(case)
#                 curr = case

#         curr = to_visit_queue.get()

#     path = get_parents(curr, goal, parents)
#     print(path)


def main() -> int:

    ## data given
    rows = 5
    cols = 7
    start = (cols - cols, rows - rows)
    goal = (cols - 1, rows - 1)
    obstacles = {
        (1, 4),
        (1, 4),
        (3, 0),
        (3, 1),
        (3, 2),
        (3, 3),
        (3, 4),
        (3, 4),
        (5, 0),
        (5, 1),
    }

    ## grid creaction
    grid = Grid(rows, cols)
    grid.display()

    ## Build the maze (source, dest, obstacle)
    maze = Maze(grid, (1,2), (5,3), obstacles)
    path = maze.solve_bfs()
    maze.display_path(path)


    return 0


if __name__ == "__main__":
    main()
