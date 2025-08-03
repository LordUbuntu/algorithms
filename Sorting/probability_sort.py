# Jacobus Burger (2023)
# Probability sort:
#   This is one I came up with on my own. Bogosort is
#   totally random, but if we temper the randomness it
#   can make a probibalistic sort that can sort numbers
#   even if it doesn't necessarily know what all the
#   numbers are.
# How it works:
#   We start with the smallest and largest numbers
#   known, placing the smallest at the start and the
#   biggest at the end.
#   Then we select a random number between the ends.
#       Based on the difference, we place the number
#       somewhere in the array based on how close it is
#       to the other numbers given some standard
#       deviation, and pick up whatever number was in
#       that place already. Then we keep repeating this
#       process until the distribution of numbers in the
#       array has small numbers trending to the
#       beginning, big numbers trending to the end, and
#       median numbers trending to the middle.
#   The fun part of this is that without knowing any
#   values besides the start, end, and difference, we can eventually
#   reach a high (but not absolute) certainty that
#   numbers are in the right order which increases given
#   more time to "sort" the numbers, and as the
#   "randomness" cools down. This also has the fun
#   consequence of guaranteeing a sorted array given a
#   smaller infinite time than bogosort while still
#   being random.


# Is this a practical idea? Seems like it would be O(n^2), maybe O(n log n) at best.
