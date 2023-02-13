

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


def djikstra(G, source, sink):
    # TODO - check added cost before visiting vertices instead of after
    unvisited = [[source, 0]]
    visited = []

    while unvisited:
        v, cost = unvisited.pop(0)
        if v not in visited:
            visited.append(v)
            for w, c in G[v]:
                if w in visited:
                    continue
                unvisited.append([w, cost + c])
            if v == sink:
                return [visited, cost]
    return [None, float("inf")]
