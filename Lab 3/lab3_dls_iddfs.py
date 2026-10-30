graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
def dls(node, goal, depth_limit):
    if node == goal:
        return "FOUND"
    if depth_limit <= 0:
        return "CUTOFF"   
    cutoff_occurred = False
    for neighbor in graph.get(node, []):
        result = dls(neighbor, goal, depth_limit - 1)
        if result == "FOUND":
            return "FOUND"
        if result == "CUTOFF":
            cutoff_occurred = True        
    return "CUTOFF" if cutoff_occurred else "FAILURE"
def iddfs(start, goal, max_depth):
    for limit in range(1, max_depth + 1):
        result = dls(start, goal, limit)
        print("Limit", limit, ":", result)
        if result == "FOUND":
            return
iddfs('A', 'F', 4)