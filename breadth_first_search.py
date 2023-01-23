# Jacobus Burger (2023)
# Breadth First Search algorithm on a graph G

G = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'G'],
    'C': ['A', 'F'],
    'D': ['A', 'E', 'F'],
    'E': ['D'],
    'F': ['C', 'D'],
    'G': ['B'],
}


def bfs(G, v):
    visited, queue = {v}, [v]
    while queue:
        v = queue.pop(0)
        visited.add(v)
        for w in G[v]:
            if w not in visited:
                queue.append(w)
    return visited
