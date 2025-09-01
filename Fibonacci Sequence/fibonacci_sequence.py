# Jacobus Burger (2025-08-29)
# Fibonacci Sequence (Python 3.13)
# Description:
# Fibonacci Sequence is a recursive mathematical sequence where every
#   subsequent value Fn = Fn-1 + Fn-2. It often starts like F0 = F1 = 1,
#   interestingly it works bi-directionally in both positive and negative
#   values for n.
#                               F0 F1
#   13, -8, 5, -3, 2, -1, 1, 0, 1  1  2 3 5 8 13 ...
# Info:
# - https://en.wikipedia.org/wiki/Fibonacci_sequence
# - https://rosettacode.org/wiki/Fibonacci_sequence#Python


def fibonacci(n: int) -> int:
    # TODO: make work for all int
    # - how would i make this work on negatives?
    if n <= 1:
        return 1

    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    n = int(input())
    print("fib {} = {}".format(n, fibonacci(n)))
