# Jacobus Burger (2023)
# Depth First Search algorithm on a graph G

G = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'G'],
    'C': ['A', 'F'],
    'D': ['A', 'E', 'F'],
    'E': ['D'],
    'F': ['C', 'D'],
    'G': ['B'],
}


# G is graph, v is starting vertex
# most straigh-forward solution
def dfs(G, v):
    visited, stack = {v}, [v]
    while stack:
        v = stack.pop()
        visited.add(v)
        for w in G[v]:
            if w not in visited:
                stack.append(w)
    return visited
