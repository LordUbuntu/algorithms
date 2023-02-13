

# should go A -> B -> C -> F for total weight of 4 (< 5 or 6)
G = {
    'A': [['B', 1]],
    'B': [['A', 1], ['C', 1], ['D', 3]],
    'C': [['B', 1], ['E', 2]],
    'D': [['B', 3], ['E', 1]],
    'E': [['C', 2], ['D', 1]]
}

# or as dict comprehension with input of form:
# from to weight
# eg:
# A B 1 => {'A': [('B', 1)]}
# use a min-heap priority queue (heapq) to automatically order next
#   vertices in queue by priority of least to most weight (added cost)
from heapq import heappush as enque
from heapq import heappop as deque


def djikstra(G, source, sink):
    # TODO - check added cost before visiting vertices instead of after
    unvisited = [[source, 0]]
    visited = []

    while unvisited:
        v, cost = deque(unvisited)
        if v not in visited:
            visited.append(v)
            for w, c in G[v]:
                if w in visited:
                    continue
                enque(unvisited, [w, cost + c])
            if v == sink:
                return cost
    return -1
