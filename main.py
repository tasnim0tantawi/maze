from maze import Maze
from math import sqrt
from colorama import Fore

print(Fore.LIGHTYELLOW_EX + "Welcome to the Maze Generator!")
print(Fore.LIGHTBLUE_EX + "Please enter the number of rows and columns for the maze.")
rows = int(input("Rows: "))
columns = int(input("Columns: "))
print(Fore.LIGHTBLUE_EX + "Please enter the percentage of barriers for the maze.")
barriers = int(input("Barriers: "))
while barriers > 50 or barriers < 0:
    print(Fore.LIGHTRED_EX + "Please enter a number between 0 and 50.")
    barriers = int(input("Barriers: "))

print(Fore.LIGHTBLUE_EX + "Please enter the starting coordinates for the maze.")
# start is a tuple of (row, column)
start = (int(input("Start Row: ")), int(input("Start Column: ")))
print(Fore.LIGHTBLUE_EX + "Please enter the ending coordinates for the maze.")
# end is a tuple of (row, column)
end = (int(input("End Row: ")), int(input("End Column: ")))
maze = Maze(rows, columns, barriers, start, end)
print(Fore.LIGHTYELLOW_EX + "Here is your maze:")
print(maze.print_maze())
