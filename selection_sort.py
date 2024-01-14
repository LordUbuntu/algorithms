# Jacobus Burger (2023)
# A simple selection sort algorithm

def sort(l: list) -> list:
    for current in range(len(l)):
        minimum = current  # assume minimum is first element
        # search for a smaller value after current
        for index in range(current + 1, len(l)):
            if l[index] < l[minimum]:
                minimum = index
        # swap elements
        l[current], l[minimum] = l[minimum], l[current]
    return l
