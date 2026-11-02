graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(node, goal, visited=None):
    if visited is None:
        visited = set()

    if node == goal:
        return True

    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor, goal, visited):
                return True

    return False

print(dfs('A', 'F'))