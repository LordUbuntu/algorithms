# Jacobus Burger (2023)
# Info:
#   Algorithms to compare different arrangements of letters in a string
from string import ascii_lowercase

# has all the letters of the alphabet
def pangram(a):
    if set(a.lower()) == set(ascii_lowercase):
        return True
    return False
