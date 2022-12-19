import random
from math import sqrt
from search import astar

# a class to represent what a maze cell is. Like a cell data type to create objects from.
# It can be an empty cell, a barrier, a start, an end (goal), or a path.
# start is marked with an S, end (goal) is marked with an S
# barriers are marked with a ■, and paths are marked with a ●


class Cell:
    EMPTY = " "
    BARRIER = "■"
    START = "S"
    END = "★"
    PATH = "●"


class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column


class Maze:
    def make_grid(self):
        grid = []
        for row in range(self.rows):
            grid.append([])
            for column in range(self.columns):
                grid[row].append(Cell.EMPTY)
        return grid

    def add_barriers(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if random.randint(0, 100) < self.barriers:
                    self.grid[row][column] = Cell.BARRIER

    def __init__(self, rows, columns, barriers, start, end):
        self.rows: int = rows
        self.columns: int = columns
        self.barriers: int = barriers
        self.start: tuple = start
        self.end: tuple = end
        self.grid = self.make_grid()
        self.add_barriers()
        self.grid[self.start[0]][self.start[1]] = Cell.START
        self.grid[self.end[0]][self.end[1]] = Cell.END

        self.path = []
        self.visited = []
        self.stack = []

    def print_maze(self):
        """ Prints the maze """
        #  Add the top border
        maze_string = ""
        maze_string += "╔" + "═" * (self.columns * 2 + 1) + "╗\n"
        # The maze is a grid of cells
        for row in self.grid:
            # Add the left border
            maze_string += "║ "
            for cell in row:
                maze_string += cell + " "
            maze_string += "║\n"
            # Add the right border
        maze_string += "╚" + "═" * (self.columns * 2 + 1) + "╝\n"
        # Add the bottom border
        return maze_string

    def locations_to_move(self, row, column):
        locations = []
        if row + 1 < self.rows and self.grid[row + 1][column] != Cell.BARRIER:
            locations.append((row + 1, column))
        if row - 1 >= 0 and self.grid[row - 1][column] != Cell.BARRIER:
            locations.append((row - 1, column))
        if column + 1 < self.columns and self.grid[row][column + 1] != Cell.BARRIER:
            locations.append((row, column + 1))
        if column - 1 >= 0 and self.grid[row][column - 1] != Cell.BARRIER:
            locations.append((row, column - 1))
        return locations

    def visit(self, path):
        # path is a list of tuples of (row, column)
        for location in path:
            # Only mark the location as visited if it is not the start or end
            if self.grid[location[0]][location[1]] != Cell.START and self.grid[location[0]][location[1]] != Cell.END:
                self.grid[location[0]][location[1]] = Cell.PATH

    def is_goal(self, row, column):
        return row == self.end[0] and column == self.end[1]

    def manhattan_distance(self, row, column):
        """ Manhattan distance is the sum of the absolute values of the differences of the coordinates.
         It is the first heuristic we will use to solve the maze. """
        def distance():
            x = abs(row - self.end[0])
            y = abs(column - self.end[1])
            return abs(x + y)
        return distance

    def euclidean_distance(self, row, column):
        def distance():
            x = abs(row - self.end[0])
            y = abs(column - self.end[1])
            return sqrt((x ** 2 + y ** 2))
        return distance

    def solve(self):
        heuristic_distance = self.manhattan_distance(self.start[0], self.start[1])
        self.path = astar(self.start, self.is_goal, self.locations_to_move, heuristic_distance)
        self.visit(self.path)
        return self.path


