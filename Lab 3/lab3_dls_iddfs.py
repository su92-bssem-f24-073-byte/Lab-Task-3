graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path
    if limit <= 0:
        return "CUTOFF", None
    
    cutoff_occurred = False
    for neighbor in graph[node]:
        result, res_path = dls(neighbor, goal, limit - 1, path + [neighbor])
        if result == "FOUND":
            return "FOUND", res_path
        if result == "CUTOFF":
            cutoff_occurred = True
            
    return ("CUTOFF" if cutoff_occurred else "FAILURE"), None

def iddfs(start, goal, max_depth):
    for depth in range(max_depth + 1):
        result, path = dls(start, goal, depth, [start])
        print(f"Limit {depth}: Status = {result}, Path = {path}")
        if result == "FOUND":
            return path
    return None

if __name__ == "__main__":
    print("--- Task 2: DLS & IDDFS Test (Limits 1 to 4) ---")
    iddfs("A", "G", 4)