# Jacobus Burger (2023)
# Depth First Search algorithm on a graph G


# looks like
#     D
#  B     E
# A C   F G
G = {
    'A': ['B', 'H'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['B'],
    'D': ['B'],
    'E': ['B', 'F', 'G'],
    'F': ['E'],
    'G': ['E'],
    'H': ['A', 'I'],
    'I': ['H'],
}


# G is graph, v is starting vertex
# most straigh-forward solution
def dfs(G, v):
    visited, stack = [], [v]
    while stack:
        v = stack.pop()
        visited.append(v)
        for w in reversed(G[v]):
            if w not in visited:
                stack.append(w)
    return visited
