# Jacobus Burger (2023)
# Info:
#   Algorithms to compare different arrangements of letters in a string

# was "annagram" the term for a string that can arranged into another (not necessarily read the same forwards as backwards)
def same_letters(a, b):
    if sorted(a) == sorted(b):
        return True
    return False


# what was the term for a string that is the reversed version of another?
def same_reversed(a, b):
    if a == reversed(b):
        return True
    return False
