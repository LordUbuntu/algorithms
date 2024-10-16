# Jacobus Burger (2024-09-03)
# Flattens a higher dimensional data structure into one dimension


# nieve solution assuming a generator (Python specific)
def flatten(generator):
    return [*generator]


def flat(L):
    # for a 2d list [[][]]
    return [*l for l in L]
