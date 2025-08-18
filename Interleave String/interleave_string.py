# Jacobus Burger (2025-06-09)
# Interleaving data of two strings, though the same principle can
#      be applied to any sequence/array data type (though the
#      implementation will differ between them)
# see:
# - https://en.wikipedia.org/wiki/Interleaving_(data)
from sys import argv


# Time Complexity: O(n) where n is longer string
# Space Complexity: O(nm)
def interleave(a: str, b: str) -> str:
    # i love snakelang 🐍
    return ''.join([a + b for a, b in zip(a, b)])


if __name__ == "__main__":
    # make sure args are provided
    if len(argv) < 3:
        exit(1)
    # get a and b from argv
    a = argv[1]
    b = argv[2]
    # interleave a and b
    c = interleave(a, b)
    # print results
    print("{}\n{}\n{}\n\n".format(a, b, c))
