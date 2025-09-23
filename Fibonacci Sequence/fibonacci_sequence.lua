--[[
  Jacobus Burger (2025-09-23)
  Fibonacci Sequence (Lua 5.4)
  Fibonacci Sequence is a recursive mathematical sequence where every
    subsequent value Fn = Fn-1 + Fn-2. It often starts like F0 = F1 = 1,
    interestingly it works bi-directionally in both positive and
    negative values for n.
                             F0 F1
    13, -8, 5, -3, 2, -1, 1, 0, 1  1  2 3 5 8 13 ...
  Info:
  - https://en.wikipedia.org/wiki/Fibonacci_sequence
  - https://rosettacode.org/wiki/Fibonacci_sequence#Lua
]]


function fibonacci(n)
  local a, b = 0, 1
  for _ = 1, n do
    a, b = b, a + b
  end
  for _ = n, 1, -1 do
    a, b = b - a, a
  end
  return a
end


function main()
  local n = io.read("n")
  print(fibonacci(n))
  print(string.format("fib %i = %i", n, fibonacci(n)))
end


main()
