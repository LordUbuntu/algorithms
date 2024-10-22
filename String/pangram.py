# Jacobus Burger (Oct 2024)
# Algorithm:
#   Pangram
# Desc:
#   An algorithm that determines if a string has every letter of the
#   alphabet in it.
# Info:
#   https://en.wikipedia.org/wiki/Pangram
from string import ascii_lowercase

# has all the letters of the alphabet
def pangram(a):
    if set(a.lower()) == set(ascii_lowercase):
        return True
    return False
