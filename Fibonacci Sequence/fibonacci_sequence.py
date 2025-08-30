# Jacobus Burger (2025-08-29)
# Fibonacci Sequence (Python 3.13)
# Description:
# Fibonacci Sequence is a recursive mathematical sequence where every
#   subsequent value Fn = Fn-1 + Fn-2. It often starts like
#   1 1 2 3 5 8 13 ...
# Info:
# - https://en.wikipedia.org/wiki/Fibonacci_sequence
# - https://rosettacode.org/wiki/Fibonacci_sequence#Python
from sys import argv


def fibonacci(n: int) -> int:
    if n <= 1:
        return 1

    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    if (len(argv) < 2):
        exit(1)
    n = int(argv[1])
    print("fib {} = {}".format(n, fibonacci(n)))
