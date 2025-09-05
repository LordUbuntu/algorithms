# Jacobus Burger (2025-08-29)
# Triangle Numbers (Uiua 0.16)
# Description:
# Triangle Numbers are a count of the number of objects arranged in
#   an equilateral traingle for a given row number.
#    .    1 = 1
#   . .   2 = 3
#  . . .  3 = 6
# . . . . 4 = 10
#  etc...
# Info:
# - https://en.wikipedia.org/wiki/Triangular_number

# TriangleNumber = reduce add range add 1
# add 1 = incremet argument by 1 (extend range by 1)
# range = generate an array of natural numbers
# reduce add = sum numbers in array together
TriangleNumbers ← /+⇡+1

# Main = &p TriangleNumbers parse &sc
# &sc = scan input line as string
# parse = parse input as number
# TriangleNumbers = call traingleNumbers with values on stack
# &p = print resulting value on stack to output
Main ← &p TriangleNumbers ⋕ &sc

Main
