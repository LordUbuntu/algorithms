# Jacobus Burger (2025-09-04)
# Triangle Numbers (Python 3.13)
# Description:
# Triangle Numbers are a count of the number of objects arranged in
#   an equilateral traingle for a given row number.
#    .    1 = 1
#   . .   2 = 3
#  . . .  3 = 6
# . . . . 4 = 10
#  etc...
# Info:
# - https://en.wikipedia.org/wiki/Triangular_number


def triangle_numbers(n: int) -> int:
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


if __name__ == "__main__":
    n = int(input())
    print(triangle_numbers(n))
