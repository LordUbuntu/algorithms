# Jacobus Burger (2022)
# Info:
#   Python equivalent of the C program by the same name


# I love snakelang
def reverse(array):
    return array[::-1]


if __name__ == '__main__':
    array = [i for i in range(1, 17)]
    print(array, reverse(array))
