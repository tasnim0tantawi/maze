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
        # g(n) + h(n) is f(n) in the A* algorithm
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def path_generator(self):
        """ Generates the path from the start node to the end node """
        pass


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

    def __str__(self):
        return str(self.queue)
