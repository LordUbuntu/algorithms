# Jacobus Burger (Oct 2024)
# Algorithm:
#   Palindrome
# Desc:
#   An algorithm that sees if two strings are reversals of eachother
# Info:
#   https://en.wikipedia.org/wiki/Palindrome
def palindrome(a, b):
    if a == reversed(b):
        return True
    return False
