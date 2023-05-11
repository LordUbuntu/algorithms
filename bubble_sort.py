# Jacobus Burger (2022)
# Bubble Sort
# Bubble sort compaires pairs of adjacent values and swaps them
# if they're out of order. It's worst case is O(n^2), not great.
def sort(l: list) -> list:
    result = l.copy()
    for _ in range(1, len(result)):
        sorted = True
        for index in range(1, len(result)):
            if result[index - 1] >= result[index]:
                sorted = False
                result[index - 1], result[index] = result[index], result[index - 1]
        if sorted == True:
            break
    return result
