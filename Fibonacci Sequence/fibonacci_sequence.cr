# Jacobus Burger (2025-08-29)
# Fibonacci Sequence (Crystal 1.17)
# Description:
# Fibonacci Sequence is a recursive mathematical sequence where every
#   subsequent value Fn = Fn-1 + Fn-2. It often starts like F0 = F1 = 1,
#   interestingly it works bi-directionally in both positive and negative
#   values for n.
#                               F0 F1
#   13, -8, 5, -3, 2, -1, 1, 0, 1  1  2 3 5 8 13 ...
# Info:
# - https://en.wikipedia.org/wiki/Fibonacci_sequence
# - https://rosettacode.org/wiki/Fibonacci_sequence#Crystal
require "big"


def fibonacci(n : Int64)
  # TODO: make work for all int
  return n if n <= 1
  a, b = BigInt.new(1), BigInt.new(1)
  (n - 1).times do
    a, b = b, a + b
  end
  b
end


def main
  n : Int64 = gets.try(&.to_i64) || 0_i64
  print "fib #{n} = #{fibonacci(n)}\n"
end


main
