import heapq

def a_star(start, goal, graph):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = start
    cost_so_far[start] = 0
    
    path=[]
    while frontier:
        current = heapq.heappop(frontier)[1]
        path.append(current)
        
        if current == goal:
            break
        
        for next,cost in graph[current]:
            new_cost = cost_so_far[current] + cost
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + (heuristic[goal] + heuristic[next])
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current
    
    print(path)

graph = {
    
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1),('H', 7)] ,
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],

}

heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}

a_star('A', 'J', graph)
