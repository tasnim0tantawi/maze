from maze import Maze
from colorama import Fore, Style

print(Fore.LIGHTYELLOW_EX + "Welcome to the Maze Generator!")
print(Fore.LIGHTBLUE_EX + "Please enter the number of rows and columns for the maze.")
rows = int(input("Rows: "))
columns = int(input("Columns: "))
while rows < 5 or columns < 5:
    print(Fore.RED + "The number of rows and columns must be at least 5.")
    rows = int(input("Rows: "))
    columns = int(input("Columns: "))

print(Fore.LIGHTBLUE_EX + "Please enter the percentage of barriers for the maze.")
barriers = int(input("Barriers: %"))
while barriers > 40 or barriers < 0:
    print(Fore.LIGHTRED_EX + "Please enter a number between 0 and 40.")
    barriers = int(input("Barriers: "))

print(Fore.LIGHTBLUE_EX + "Please enter the starting coordinates for the maze.")
# start is a tuple of (row, column)
start = (int(input("Start Row: ")), int(input("Start Column: ")))
while start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= columns:
    print(Fore.LIGHTRED_EX + "Please enter a valid starting coordinate.")
    start = (int(input("Start Row: ")), int(input("Start Column: ")))

print(Fore.LIGHTBLUE_EX + "Please enter the ending coordinates for the maze.")
# end is a tuple of (row, column)
end = (int(input("End Row: ")), int(input("End Column: ")))
maze = Maze(rows, columns, barriers, start, end)
while end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= columns:
    print(Fore.LIGHTRED_EX + "Please enter a valid ending coordinate.")
    end = (int(input("End Row: ")), int(input("End Column: ")))

print(Fore.LIGHTYELLOW_EX + "Here is your maze:")
print(maze.print_maze())
print(Fore.LIGHTBLUE_EX + "Here is the solution:" + Fore.RESET)
maze.solve()

