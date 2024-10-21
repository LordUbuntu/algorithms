# rearragements of a word
def anagram(a, b):
    if sorted(a) == sorted(b):
        return True
    return False
