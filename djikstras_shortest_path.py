

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
        if v == sink:
            return cost
        if v not in visited:
            visited.append(v)
            for w, c in G[v]:
                if w in visited:
                    continue
                enque(unvisited, [w, cost + c])
    return -1





# same algorithm, but with a different measure of the distances from
#   the start node to the end node.
# inspired by https://www.youtube.com/watch?v=niB1tTeC2yI&t=318s
import heapq
def alt_djikstra(G, start):
    distance = {start: 0}  # distance from start to a given node
    visited = set()
    priority_queue = [(start, 0)]
    while priority_queue:
        node, weight = heapq.heappop(priority_queue)
        if node in visited:
            continue
        for adj_node, adj_distance in G[node]:
            if adj_node not in distance \
            or distance[node] + adj_distance < distance[adj_node]:
                distance[adj_node] = adj_distance
                heapq.heappush(priority_queue, (adj_node, distance[adj_node]))
    return distance
