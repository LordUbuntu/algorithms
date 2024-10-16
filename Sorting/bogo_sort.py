# Jacobus buger (Oct 2024)
from random import randint


def sort(array: list) -> list:
    while array != sorted(array):
        i = randint(0, len(array) - 1)
        j = randint(0, len(array) - 1)
        array[i], array[j] = array[j], array[i]
    return array
