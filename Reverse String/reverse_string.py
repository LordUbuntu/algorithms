# Jacobus Burger (2022)
# Reverse a string (Python 3)
# Description:
# Reverse characters in a string. The principles behind this can
#   be generalized on a string of any data type (strings do not
#   have to be a string of characters).
# There's many approaches to doing this. One approach is to modify
#   an existing array provided, another is to create and return a new
#   array, and more.
# Info:
# - https://en.wikipedia.org/wiki/String_(computer_science)#Reversal
# - https://rosettacode.org/wiki/Reverse_a_string


# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_a(array):
    # I love snakelang
    return array[::-1]


# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_b(array):
    # iterate from end to start so s1_0 == s2_n, s1_1 == s2_n-1, etc
    result = []
    for i in range(len(array), -1, -1):
        result.append(array[i])
    return result


if __name__ == '__main__':
    array = [i for i in range(1, 17)]
    print(array, reverse_b(array))
