# Jacobus Burger (2023)
# Breadth First Search algorithm on a graph G
from collections import deque


# looks like
#     A
#   B   C
#  D E F G
#
# should return
# ABCDEFG
G = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}


def bfs(G, v):
    visited, queue = [v], deque([v])
    while queue:
        v = queue.popleft()
        for w in G[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return visited
