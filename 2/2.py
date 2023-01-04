import heapq

# Represents a node in the search tree
class Node:
    def __init__(self, state, cost, heuristic, parent):
        self.state = state
        self.cost = cost
        self.heuristic = heuristic
        self.parent = parent

    def __lt__(self, other):
        # Compare nodes based on their total cost
        return self.cost + self.heuristic < other.cost + other.heuristic

# Represents a graph as a dictionary of nodes
class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def get_successors(self, node):
        return self.edges[node]

# AO* search algorithm
def ao_star_search(graph, start, goal, heuristic, weight=1.0):
    # Create a priority queue for storing nodes
    frontier = []
    heapq.heappush(frontier, (0, Node(start, 0, heuristic(start), None)))

    # Create a set for storing visited nodes
    visited = set()

    while frontier:
        # Get the node with the lowest total cost
        current_cost, current_node = heapq.heappop(frontier)

        # If the node is the goal, return the path
        if current_node.state == goal:
            path = []
            while current_node is not None:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        # Mark the node as visited
        visited.add(current_node.state)

        # Add the neighboring nodes to the queue
        for state, cost in graph.get_successors(current_node.state):
            if state not in visited:
                total_cost = current_node.cost + cost + weight * heuristic(state)
                heapq.heappush(frontier, (total_cost, Node(state, current_node.cost + cost, heuristic(state), current_node)))

# Example usage
nodes = ['A', 'B', 'C', 'D', 'E']
edges = {
    'A': [[('B', 1),('F',7)], ('C', 2)],
    'B': [('D', 3), ('E', 4)],
    'C': [('D', 5), ('E', 6)],
    'D': [],
    'E': []
}
graph = Graph(nodes, edges)
start = 'A'
goal = 'E'

# A heuristic function that calculates the straight-line distance to the goal
def heuristic(state):
    if state == 'A':
        return 10
    elif state == 'B':
        return 9
    elif state == 'C':
        return 8
    elif state == 'D':
        return 7
    elif state == 'E':
        return 6

print(ao_star_search(graph, start, goal, heuristic))
