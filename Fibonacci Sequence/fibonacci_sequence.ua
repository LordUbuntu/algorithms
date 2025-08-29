

# Fib = dip pop repeat ( off add ) dip both 1
# Fib N => call Fib with N on top of stack
# dip both 1 => set stack below N to [1 1], stack becomes [N 1 1]
# repeat ( off add ) => repeat N times adding values of stack
#   keeping previous below, thus iterating over fibonacci sequence
# dip pop => remove the top value leaving the result of the fibonacci
#   sequence function as the remaining value on the stack
Fib ← ⊙ ◌⍥ (⤚+)⊙ ∩1

# &p Fib parse &sc
# &sc => read input from stdin
# parse => parse string from stdin as a number
# Fib => call Fib with top value on stack being N
# &p => print top value on stack to stdout
&p Fib ⋕ &sc
