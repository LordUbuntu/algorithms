# Jacobus Burger (2024)
# Functional Algorithms and Data Structures


def filter(f, arr):
    result = []
    for val in arr:
        if f(val):
            result.append(val)
    return result


def map(f, arr):
    result = []
    for val in arr:
        result.append(f(val))
    return result


def reduce(f, arr, init=None):
    result = 0 if init is None else init
    for val in arr:
        result = f(result, val)
    return result


def apply(f, arr):
    result = []
    for val in arr:
        result.append(f(val))
    return result
