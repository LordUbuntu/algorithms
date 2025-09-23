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
