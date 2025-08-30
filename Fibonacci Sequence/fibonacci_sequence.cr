# Jacobus Burger (2025-08-29)
# Fibonacci Sequence (Crystal 1.17)
# Description:
# Fibonacci Sequence is a recursive mathematical sequence where every
#   subsequent value Fn = Fn-1 + Fn-2. It often starts like
#   1 1 2 3 5 8 13 ...
# Info:
# - https://en.wikipedia.org/wiki/Fibonacci_sequence
# - https://rosettacode.org/wiki/Fibonacci_sequence#Crystal


def fibonacci(n: Int64)
  return n if n <= 1
  a, b = 0, 0
  n.times do
    a, b = b, a + b
  end
  b
end


def main
  n = gets.try(&.to_i) || 0
  print "fib #{n} = #{fibonacci(n)}"
end
