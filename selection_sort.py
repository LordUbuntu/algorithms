# Jacobus Burger (2023)
# A simple selection sort algorithm

def sort(l: list) -> list:
    for current in range(len(l)):
        min = current  # assume min is first element
        # search for a smaller value in the indices after current
        for index in range(current + 1, len(l)):
            if l[index] < l[min]:
                min = index
        # swap elements if min is a different greater index
        l[current], l[min] = l[min], l[current]
    return l
