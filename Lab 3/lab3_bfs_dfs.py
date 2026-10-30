graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(graph, start, goal):
    visited = []
    queue = [[start]]
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in visited:
            visited.append(node)
            if node == goal:
                return path
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

def dfs(graph, start, goal):
    visited = []
    stack = [[start]]
    
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node not in visited:
            visited.append(node)
            if node == goal:
                return path
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    return None

print("BFS Path:", bfs(graph, 'A', 'F'))
print("DFS Path:", dfs(graph, 'A', 'F'))