# Jacobus Burger (2023)
# Info:
#   Algorithms to compare different arrangements of letters in a string

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
