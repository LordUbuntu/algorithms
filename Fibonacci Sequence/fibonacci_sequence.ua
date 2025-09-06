# Jacobus Burger (2025-08-27)
# Fibonacci Sequence (Uiua v0.16.2)
# Description:
# Fibonacci Sequence is a recursive mathematical sequence where every
#   subsequent value Fn = Fn-1 + Fn-2. It often starts like F0 = F1 = 1,
#   interestingly it works bi-directionally in both positive and negative
#   values for n.
#                            F0 F1
#   13, -8, 5, -3, 2, -1, 1, 0, 1  1  2 3 5 8 13 ...
# Info:
# - https://en.wikipedia.org/wiki/Fibonacci_sequence
# - https://rosettacode.org/wiki/Fibonacci_sequence#Uiua

# Fib = dip pop repeat ( off add ) dip fork 0 1
# Fib N = call Fib with N on top of stack
# dip fork 0 1 = ignore stack of [0 1] so N can be provided to repeat
# repeat ( off add ) = repeat N times adding values of stack keeping
#   previous value below, thus iterating the fibonacci sequence. Note
#   that Uiua has a robust function inversion system that allows this
#   to work for both positive and negative values of N, in the case of
#   negative values it will invert ( off add ) into ( with backward sub )
#   thus performing the negative extended fibonacci sequence without any
#   code change needed!
# dip pop = remove the top value leaving the result of the fibonacci
#   sequence function as the remaining value on the stack
Fibonacci ← ⊙◌⍥(⤚+)⊙⊃0 1

# Main = &p Fib parse &sc
# &sc = read input from stdin
# parse = parse string from stdin as a number
# Fib = call Fib with top value on stack being N
# &p = print top value on stack to stdout
Main ← &p $"_ = _"⊃($"fib _")(Fibonacci) ⋕&sc

Main
