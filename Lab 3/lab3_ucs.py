import heapq
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4), ('E', 1)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}
def ucs(graph, start, goal):
    queue = [(0, start, [start])]
    visited = set()   
    while queue:
        cost, node, path = heapq.heappop(queue)        
        if node not in visited:
            visited.add(node)
            if node == goal:
                return cost, path
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))
    return float("inf"), []
cost, path = ucs(graph, 'A', 'F')
print("Path:", path)
print("Cost:", cost)