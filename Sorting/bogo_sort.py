from random import randint


def bogo(arr: list) -> list:
    while arr != sorted(arr):
        i = randint(0, len(arr) - 1)
        j = randint(0, len(arr) - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
