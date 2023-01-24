# Jacobus Burger (2023)
# Breadth First Search algorithm on a graph G

G = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'F'],
    'C': ['G'],
    'D': [],
    'E': [],
    'F': ['H', 'I'],
    'G': [],
    'H': [],
    'I': []
}


def bfs(G, v):
    visited, queue = {v}, [v]
    while queue:
        v = queue.pop(0)
        visited.add(v)
        for w in G[v]:
            if w not in visited:
                queue.append(w)
    return list(visited)
