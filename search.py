import heapq


class Node:
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


def astar(initial, goal_test,  # a function that takes a row and column and returns true if it is the goal
          to_visit,  # a function
          heuristic  # a function, it is either manhattan_distance or euclidean_distance
          ):
    """  A* algorithm is an informed/heuristic search algorithm that uses a heuristic value to solve the maze.
        It is a combination of the breadth-first search algorithm and the depth-first search algorithm.
        It uses a priority queue to keep track of the cells to visit in an open list. """

    # The priority queue is a list of tuples of (distance, row, column)
    open_list = PriorityQueue()
    open_list.push(Node(initial, 0, heuristic()))
    # The closed list is a list of tuples of (row, column)
    closed_list = {initial: 0}

    while not open_list.empty():
        current_node = open_list.pop()
        current_state = current_node.state
        # If the current node is the goal node, then return it
        if goal_test(current_state[0], current_state[1]):
            return current_node
        for child in to_visit(current_state[0], current_state[1]):
            new_cost = current_node.cost + 1
            # If the child is not in the closed list, then add it to the open list
            if child not in closed_list or new_cost < closed_list[child]:
                closed_list[child] = new_cost
                open_list.push(Node(child, new_cost, heuristic(), current_node))
    return None
