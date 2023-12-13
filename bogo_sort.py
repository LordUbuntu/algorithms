# TODO: use choice?
from random import randint as rand
from time import sleep


def bogo(arr: list) -> list:
    while arr != sorted(arr):
        for i in range(len(arr)):
            pick = rand(0, len(arr) - 1)
            arr[i], arr[pick] = arr[pick], arr[i]
        print(arr)
        sleep(1)
    return arr


if __name__ == "__main__":
    bogo([3, 5, 4, 2, 1])
