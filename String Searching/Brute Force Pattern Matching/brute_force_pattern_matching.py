# Jacobus Burger (2025-08-23)
# Brute Force Pattern Matching (Python 3.13)
# Brute Force Pattern Matching is a brute force approach to matching
#      a substring of a larger string of contiguous data. It does so
#      by comparing the first letter of the substring with the current
#      letter in the string until it finds a match, then compares to
#      see that the substring and that section of the string both
#      match. This is an obvious approach, but isn't very effective
#      when compared to more clever approaches.
# Pattern Matching has a lot of great applications in multiple
#      disciplines, such as for bioinformatics.
# Info:
# - https://en.wikipedia.org/wiki/String-searching_algorithm#Naive_string_search
# - https://www.youtube.com/watch?v=u6MgvwO8m_8
# - https://www.youtube.com/watch?v=yKhPWrdA6U8
from os import argv


def match(pattern: str, string: str) -> int:
    if len(pattern) > len(string):
        return -1
    for n in range((len(string) - len(pattern)) + 1):
        found = True
        for m in range(len(pattern)):
            if pattern[m] != string[n + m]:
                found = False
                break
        if found:
            return n
    return -1


if __name__ == "__main__":
    if len(argv) < 3:
        exit(1)
    pattern = argv[1]
    string = argv[2]
    n = match(pattern, string)
    if n < 0:
        print("no pattern match of {} in {}".format(pattern, string))
    else:
        print("match of {} in {} at {}".format(pattern, string, n))
