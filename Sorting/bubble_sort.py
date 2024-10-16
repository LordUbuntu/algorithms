# Jacobus Burger (2022)
# Bubble Sort
# Bubble sort compaires pairs of adjacent values and swaps them
#     if they're out of order. It's worst case is O(n^2). So not
#     great on big inputs but fine for smaller ones
def sort(l: list) -> list:
    for _ in range(1, len(l)):
        sorted = True
        for index in range(1, len(l)):
            if l[index - 1] >= l[index]:
                sorted = False
                l[index - 1], l[index] = l[index], l[index - 1]
        if sorted == True:
            break
    return l
