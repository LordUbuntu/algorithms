# Jacobus Burger (2023)
# Info:
#   Algorithms to compare different arrangements of letters in a string
from string import ascii_lowercase

# rearragements of a word
def anagram(a, b):
    if sorted(a) == sorted(b):
        return True
    return False


# reversal of a word
def palindrome(a, b):
    if a == reversed(b):
        return True
    return False


# has all the letters of the alphabet
def pangram(a):
    if set(a.lower()) == set(ascii_lowercase):
        return True
    return False


# used to find substrings quickly
# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm
def bmss(string, substring):
    pass
