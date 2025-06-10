from sys import argv


def interleave(a: str, b: str) -> str:
    """
    Interleave 2 strings together.

    1. zip elements together pair-wise
    2. concatenate pairs
    3. return full string
    """
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
}
