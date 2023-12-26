from random import randint
from random import sample
from time import sleep


def bogo(arr: list) -> list:
    while arr != sorted(arr):
        i = randint(0, len(list) - 1)
        j = randint(0, len(list) - 1)
        arr[i], arr[j] = arr[j], arr[i]
        print(arr)
        sleep(1)
    return arr


if __name__ == "__main__":
    bogo(sample(range(0, 100), randint(1, 30)))
