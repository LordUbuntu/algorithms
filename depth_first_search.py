# Jacobus Burger (2023)
# Depth First Search algorithm on a graph G

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


# G is graph, v is starting vertex
# most straigh-forward solution
def dfs(G, v):
    visited, stack = {v}, [v]
    while stack:
        v = stack.pop()
        visited.add(v)
        for w in reversed(G[v]):
            if w not in visited:
                stack.append(w)
    return list(visited)
