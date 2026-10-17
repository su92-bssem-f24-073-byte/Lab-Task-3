import heapq

weighted_graph = {
    "A": [("B", 1), ("C", 10)],
    "B": [("D", 2), ("E", 2)],
    "C": [("F", 5), ("G", 2)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}

def uniform_cost_search(start, goal):
    pq = [(0, start, [start])]
    visited = {}

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node in visited and visited[node] <= cost:
            continue
        visited[node] = cost

        for neighbor, weight in weighted_graph[node]:
            new_cost = cost + weight
            if neighbor not in visited or new_cost < visited.get(neighbor, float('inf')):
                heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))
                
    return None, float('inf')

if __name__ == "__main__":
    print("--- Task 3: Uniform Cost Search (UCS) ---")
    path, total_cost = uniform_cost_search("A", "G")
    print("UCS Path:", path)
    print("Total Cost:", total_cost)