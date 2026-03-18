from queue import Queue
import numpy as np
import sys
from typing_extensions import TypeVarTuple, Unpack

MARKER_GOAL = "G"
MARKER_START = "S"
MARKER_OBSTACLE = "X"


class Grid:
    def __init__(
        self,
        cols: int,
        rows: int,
        start: tuple[int, int],
        goal: tuple[int, int],
        obstacles: set[tuple[int, int]],
    ):
        self.cols = cols
        self.rows = rows
        self.start = start
        self.goal = goal
        self.obstacles = obstacles
        self.grid = self.create_grid()

    def create_grid(self) -> np.ndarray:
        grid = np.zeros((self.cols, self.rows), dtype=object)
        x_start, y_start = self.start
        x_goal, y_goal = self.goal
        grid[y_start][x_start] = MARKER_START
        grid[y_goal][x_goal] = MARKER_GOAL
        grid = self.add_obstacles_to_grid(grid)
        return grid

    def add_obstacles_to_grid(self, grid: np.ndarray) -> np.ndarray:
        for x, y in self.obstacles:
            grid[x][y] = MARKER_OBSTACLE
        return grid

    def is_in_grid(self, current: tuple[int, int]) -> bool:
        y_min = 0
        x_min = 0
        y_max = self.rows - 1
        x_max = self.cols - 1
        return (x_min <= current[1] <= x_max) and (
            y_min <= current[0] <= y_max
        )

    # def add_points(a :tuple[int,int], b : tuple[int,int]) -> tuple[int,int]:
    #     return (a[0]+b[0], a[1]+b[1])

    def get_neighbors(self, current: tuple[int, int]) -> set[tuple[int, int]] | None:

        neighbors = set()
        x, y = current
        left = (x - 1, y)
        right = (x + 1, y)
        down = (x, y + 1)
        up = (x, y - 1)

        if not self.is_in_grid(current):
            return None

        if self.is_in_grid(left):
            set.add(left)
        if self.is_in_grid(right):
            set.add(right)
        if self.is_in_grid(up):
            set.add(up)
        if self.is_in_grid(down):
            set.add(down)

        return None

    def display(self) -> None:
        for col in range(self.cols):
            for row in range(self.rows):
                print(self.grid[col][row], end=" ")
            print()


def main() -> int:

    ## data given
    rows = 5
    cols = 7
    start = (cols - cols, rows - rows)
    goal = (cols - 1, rows - 1)
    obstacles = {(1, 5), (1, 6), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)}

    ## grid creaction
    grid = Grid(rows, cols, start, goal, obstacles)
    grid.display()

    # while not (to_visit_queue.empty()):
    #     grid.



    # ## cases to visit
    # is_visited = set()
    # is_visited.add(start)
    # print(is_visited)

    # to_visit_queue: Queue = Queue()
    # to_visit_queue.put(start)

    # curr = to_visit_queue.get()
    # if curr is None:
    #     print("no path to goal")
    #     return 1

    # # get_neighbors
    # grid.get_

    # return 0


if __name__ == "__main__":
    main()
