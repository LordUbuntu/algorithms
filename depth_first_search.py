# Jacobus Burger (2023)
# Depth First Search algorithm on a graph G


# looks like
#     D
#  B     E
# A C   F G
G = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
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
                print("add: ", w)
                stack.append(w)
    return visited
