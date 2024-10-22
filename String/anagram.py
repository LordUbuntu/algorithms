# Jacobus Burger (Oct 2024)
# Algorithm:
#   Anagram
# Desc:
#   An algorithm that determines if two strings are
#   rearrangements of each other
# Info:
#   https://en.wikipedia.org/wiki/Anagram
def anagram(a, b):
    if sorted(a) == sorted(b):
        return True
    return False
