# Jacobus Burger (2023)
# Info:
#   Algorithm to check if a string is an annagram of another
def anna(original, string):
    if sorted(original) == sorted(string):
        return True
    return False
