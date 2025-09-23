# Jacobus Burger (2025-08-27)
# Reverse a string (Uiua v0.17.0-dev.2)
# Description:
# Reverse characters in a string. The principles behind this can
#   be generalized on a string of any data type (strings do not
#   have to be a string of characters).
# There's many approaches to doing this. One approach is to modify
#   an existing array provided, another is to create and return a new
#   array, and more.
# Info:
# - https://en.wikipedia.org/wiki/String_(computer_science)#Reversal
# - https://rosettacode.org/wiki/Reverse_a_string

# &p reverse &sc
# &sc => SCan input line
# reverse => reverse array on stack (in this case, a string)
# &p => print output line
&p⇌ &sc
