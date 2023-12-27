from random import randint
from random import sample
from time import sleep


def bogo(arr: list, sort_per_second: int = 1) -> list:
    while arr != sorted(arr):
        i = randint(0, len(arr) - 1)
        j = randint(0, len(arr) - 1)
        arr[i], arr[j] = arr[j], arr[i]
        print(arr)
        sleep(1 / sort_per_second)
    return arr


if __name__ == "__main__":
    sorts_per_second = int(input("how many sorts each second?"))
    bogo(sample(range(0, 100), randint(1, 30)), sorts_per_second)
