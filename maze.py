import random
from math import sqrt
from search import astar, path_generator
from colorama import Fore

CAPITAL_LETTERS = [chr(i) for i in range(65, 91)]


class Cell:
    """ A class to represent what a maze cell is. Like a cell data type to create objects from.
    It can be an empty cell, a barrier, a start, an end (goal), or a path.
    start is marked with an S, end (goal) is marked with an S
    barriers are marked with a ■, and paths are marked with a ●
    """
    EMPTY = " "
    BARRIER = Fore.CYAN + "■" + Fore.RESET
    START = "S"
    END = Fore.LIGHTRED_EX + "★" + Fore.RESET
    PATH = Fore.LIGHTYELLOW_EX + "●" + Fore.RESET


class Maze:
    """ Maze characteristics and operations. """
    def make_maze_matrix(self):
        matrix = []
        for row in range(self.rows):
            matrix.append([])
            for column in range(self.columns):
                matrix[row].append(Cell.EMPTY)
        return matrix

    def add_barriers(self):
        """ Randomly adds barriers to the maze depending on the percentage of barriers given.
        If the randomly generated number is less than the percentage of barriers, then a barrier is added.
        Else, we keep it as an empty cell.
         """
        for row in range(self.rows):
            for column in range(self.columns):
                if random.randint(0, 100) < self.barriers:
                    self.matrix[row][column] = Cell.BARRIER

    def __init__(self, rows, columns, barriers, start, end):
        self.rows: int = rows
        self.columns: int = columns
        self.barriers: int = barriers
        self.start: tuple = start
        self.end: tuple = end
        self.matrix = self.make_maze_matrix()
        self.add_barriers()
        self.matrix[self.start[0]][self.start[1]] = Cell.START
        self.matrix[self.end[0]][self.end[1]] = Cell.END

        self.path = []
        self.visited = []

    def print_maze(self):
        """ Prints the maze. """
        #  Add the top border
        maze_string = "  "
        # adding column numbers
        for i in range(self.columns):
            maze_string += f"{i} "
        maze_string += "\n"
        maze_string += Fore.CYAN + "  ╔" + "═" * (self.columns * 2 + 1) + "╗\n" + Fore.RESET
        # The maze is a grid of cells
        for row in self.matrix:
            # adding the row alphabet
            maze_string += f"{CAPITAL_LETTERS[self.matrix.index(row)]} "
            # Add the left border
            maze_string += Fore.CYAN + "║ " + Fore.RESET
            for cell in row:
                maze_string += cell + " "
            maze_string += Fore.CYAN + "║\n" + Fore.RESET
            # Add the right border
        maze_string += Fore.CYAN + "  ╚" + "═" * (self.columns * 2 + 1) + "╝\n" + Fore.RESET
        # Add the bottom border
        return maze_string

    def locations_to_move(self, row, column):
        """ Returns a list of tuples of the locations that can be moved to from the current location.
        The list is in the order of right, left, top, down. """
        locations = []
        # Check if the right cell is a barrier/border or not
        if row + 1 < self.rows and self.matrix[row + 1][column] != Cell.BARRIER:
            locations.append((row + 1, column))
        # Check if the left cell is a barrier/border or not
        if row - 1 >= 0 and self.matrix[row - 1][column] != Cell.BARRIER:
            locations.append((row - 1, column))
        # Check if the top cell is a barrier/border or not
        if column + 1 < self.columns and self.matrix[row][column + 1] != Cell.BARRIER:
            locations.append((row, column + 1))
        # Check if the bottom cell is a barrier/border or not
        if column - 1 >= 0 and self.matrix[row][column - 1] != Cell.BARRIER:
            locations.append((row, column - 1))
        return locations

    def visit(self, path):
        # path is a list of tuples of (row, column)
        for location in path:
            # Only mark the location as visited if it is not the start or end
            if self.matrix[location[0]][location[1]] != Cell.START and self.matrix[location[0]][location[1]] != Cell.END:
                self.matrix[location[0]][location[1]] = Cell.PATH

    def is_goal(self, row, column):
        """ Checks if the current location is the goal. """
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
        """ Euclidean distance is the square root of the sum of the squares of the differences of the coordinates.
         It is the second heuristic we will use to solve the maze. """
        def distance():
            x = abs(row - self.end[0])
            y = abs(column - self.end[1])
            return sqrt((x ** 2 + y ** 2))

        return distance

    def solve(self, heuristic):
        """ Solves the maze using the A* algorithm. """
        # Choose the heuristic to use
        if heuristic == "manhattan":
            heuristic_distance = self.manhattan_distance(self.start[0], self.start[1])
        else:
            heuristic_distance = self.euclidean_distance(self.start[0], self.start[1])

        solution = astar(self.start, self.is_goal, self.locations_to_move, heuristic_distance)
        if solution is None:
            print("No solution found")
        else:
            # Generate the path, by going backwards from the end to the start
            # Backtracking each node's parent
            path = path_generator(solution)
            # Add the yellow dot on the cells that represents the path on the maze
            self.visit(path)
            print(self.print_maze())
            print(f"Path length: {len(path)}")
            print("Path: " + str(path))
