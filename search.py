import heapq


class Node:
    """ To represent the node in the priority queue. """

    def __init__(self, state, cost, heuristic, parent=None):
        self.state = state
        # parent is the node that led to this node
        # it is None for the start node, that's why it is an optional parameter
        self.parent = parent
        # cost is g(n) in the A* algorithm
        self.cost = cost
        # heuristic is h(n) in the A* algorithm
        self.heuristic = heuristic

    def __lt__(self, other):
        """ This is used to compare nodes in the priority queue, less than is used to compare the total cost f(n),
        where f(n) = g(n) + h(n) in A* algorithm. """
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


class PriorityQueue:
    """ Priority Queue is a queue that sorts the items by priority,
     it uses a heap data structure to do so.
     heapq is a module that implements a heap data structure.
      The priority queue is the open list in the A* algorithm. """

    def __init__(self):
        self.queue = []

    def push(self, item):
        """ Pushes a node into the heap while making sure that the heap is still a heap.
         The heap is a binary tree, and the heap property is that the parent node is smaller than the child nodes.
         The heap property is maintained by the heapq module by doing the heapify process. """
        heapq.heappush(self.queue, item)

    def pop(self):
        """ Removes a node from the heap while making sure that the heap is still a heap.
        Using a process called heapify, the heap property is maintained. """

        return heapq.heappop(self.queue)

    def empty(self):
        return len(self.queue) == 0


def path_generator(self):
    """ Generates the path from the start node to the end node """
    path = []
    node = self
    while node is not None:
        path.append(node.state)
        node = node.parent
    return path[::-1]


def format_path(path):
    """ Prints the path. """
    count = 1
    path_string = ""
    for location in path:
        if count != len(path):
            path_string += f"{location}" + " -> "
        else:
            path_string += f"{location}"
        if count % 5 == 0:
            path_string += "\n"
        count += 1
    return path_string


def astar(start_value, is_goal,  # a function that takes a row and column and returns true if it is the goal
          to_visit,  # locations_to_move function from maze.py, returns a list of tuples of (row, column)
          # that are the locations that can be moved to from the current location
          heuristic  # a function, it is either manhattan_distance or euclidean_distance
          ):
    """  A* algorithm is an informed/heuristic search algorithm that uses a heuristic value to solve the maze.
        It is a combination of the breadth-first search algorithm and the depth-first search algorithm.
        It uses a priority queue to keep track of the cells to visit in an open list. """

    # The priority queue is a list of tuples of (distance, row, column)
    open_list = PriorityQueue()
    # We are using a priority queue so we keep track of the nodes that are closest to the goal according to
    # the heuristic
    open_list.push(Node(start_value, 0, heuristic()))
    # The closed list is a list of tuples of (row, column)
    closed_list = {start_value: 0}

    while not open_list.empty():
        # The node with the lowest cost is popped from the priority queue
        current_node = open_list.pop()
        # Current state is location is the location of the node that is popped from the priority queue
        current_state = current_node.state
        # If the current node is the goal node, then return it
        if is_goal(current_state[0], current_state[1]):
            return current_node
        # Get the locations that can be moved to from the current location to explore them
        for child in to_visit(current_state[0], current_state[1]):
            # Add g(n)=1 to the cost of the current node to get the cost of the child nodes
            new_cost = current_node.cost + 1
            # If the child node has not been visited or the new cost is less than the cost of the child node,
            # then add it to the open list to explore it
            if child not in closed_list or new_cost < closed_list[child]:
                # Saving the cost of the child node in the closed list
                closed_list[child] = new_cost
                # Putting the child nodes in the open list to explore them
                open_list.push(Node(child, new_cost, heuristic(), current_node))
    return None
    # No path found, maze is unsolvable because the goal or start is blocked by multiple barriers or too many barriers
