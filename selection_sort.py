# Jacobus Burger (2023)
# A simple selection sort algorithm

def sort(l: list) -> list:
    for current in range(len(l)):
        min = current  # assume min is first element
        # search for a smaller value after current
        for index in range(current + 1, len(l)):
            if l[index] < l[min]:
                min = index
        # swap elements
        l[current], l[min] = l[min], l[current]
    return l
