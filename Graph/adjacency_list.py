# Jacobus Burger (Oct 2024)
# Data Structure:
#   Adjacency List
# Desc:
#   An implementation of a generalized graph structure
# Info:
#   https://en.wikipedia.org/wiki/Adjacency_list

# This is a simple diamond graph example using Guido van Rossum's
#   hash table implementation approach (using a dictionary)
#
#    B
#  /   \
# A     D
#  \   /
#    C
#
G = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

class Graph:
    def __init__(self):
        self.G = {}

    def insert(self, vertex, adjacencies):
        self.G[vertex] = adjacencies

    def subgraph(self, *vertices):
        if len(vertices) == 0:
            return self.G
        subgraph = {
            vertex: self.G[vertex]
            for vertex in vertices
        }
        return subgraph

    def remove(self, vertex):
        subgraph = {vertex: self.G.pop(vertex)}
        return subgraph
