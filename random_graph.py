# Jacobus Burger (2023)
#   Various random tricks with adjacency list graph representations
G = {
    1: 2,
    2: 3,
    3: 4,
    4: 2,
    5: 3
}


# find terminal vertices (by which vertices of G have in-deg of 0)
#   working principle: left side of : are what are pointing (from),
#   while right side of : are what are being pointed at (to). Ergo, if 
#   something is pointing (in from) but not being pointed at (in to),
#   then it is a terminal vertex, assuming a convergent digraph...
def terminals(G):
    to = G.values()
    from = G.keys()
    return list(filter(lambda v: v not in to, from))


# reverse edges of a given graph G
def rev(G):
    g = {}
    for k, v in G.items():
        if v in g:
            g.update({v: [g[v], k]})
        else:
            g[v] = [k]
    return g
