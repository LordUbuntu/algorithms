

# should go A -> B -> C -> F for total weight of 4 (< 5 or 6)
G = {
    'A': [['B', 1], ['E', 6]],
    'B': [['A', 1], ['C', 1], ['D', 3]],
    'C': [['B', 1], ['E', 2]],
    'D': [['B', 3], ['E', 1]],
    'E': [['A', 6], ['C', 2], ['D', 1]]
}

# or as dict comprehension with input of form:
# from to weight
# eg:
# A B 1 => {'A': [('B', 1)]}


def djikstra(G, source, sink):
    unvisited = [[0, source]]
    visited = []

    while unvisited:
        v, cost = unvisited.pop()
        print(unvisited, visited, v, cost)
        if v in visited:
            continue
        visited.append(v)
        if v == sink:
            return cost
        for w, c in G[v]:
            if w in visited:
                continue
            unvisited.append([w, cost + c])
    return [None, float("inf")]
