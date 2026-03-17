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
        grid[x_start][y_start] = MARKER_START
        grid[x_goal][y_goal] = MARKER_GOAL
        grid = self.add_obstacles_to_grid(grid)
        return grid

    def add_obstacles_to_grid(self, grid: np.ndarray) -> np.ndarray:
        for x, y in self.obstacles:
            grid[x][y] = MARKER_OBSTACLE
        return grid

    def is_in_grid(self, current: tuple[int, int]) -> bool:
        first_row, first_col = 0
        last_row = self.rows - 1
        last_col = self.cols - 1
        return (first_row <= current[1] <= last_row) and (
            first_col <= current[0] <= last_col
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
        if self.is_in_grid(left):
            set.add(left)
        if self.is_in_grid(left):
            set.add(left)

        return None

    def display(self) -> None:
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col], end=" ")
            print()


def main() -> int:

    ## data given
    start = (0, 0)
    goal = (4, 6)
    rows = 5
    cols = 7
    obstacles = {(1, 5), (1, 6), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)}

    ## cases to visit
    is_visited = set()
    is_visited.add(start)
    print(is_visited)

    to_visit_queue: Queue = Queue()
    to_visit_queue.put(start)

    curr = to_visit_queue.get()
    if curr is None:
        print("no path to goal")
        return 1

    # get_neighbors

    ## grid creaction
    grid = Grid(rows, cols, start, goal, obstacles)
    grid.display()

    return 0


if __name__ == "__main__":
    main()
