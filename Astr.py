import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('F', 3)],
    'E': [('F', 2)],
    'F': []
}

heuristic = {
    'A': 5, 'B': 4, 'C': 3,
    'D': 2, 'E': 1, 'F': 0
}

def astar(start, goal):
    pq = [(heuristic[start], 0, start, [start])]
    best = {start: 0}

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            return path, g

        if g != best[node]:
            continue

        for neighbor, cost in graph[node]:
            new_g = g + cost

            if new_g < best.get(neighbor, float('inf')):
                best[neighbor] = new_g
                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None

print(astar('A', 'F'))