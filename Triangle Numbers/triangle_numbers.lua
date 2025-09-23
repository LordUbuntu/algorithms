--[[
 Jacobus Burger (2025-09-04)
 Triangle Numbers (Lua 5.4)
 Description:
 Triangle Numbers are a count of the number of objects arranged in
   an equilateral traingle for a given row number.
      .    1 = 1
     . .   2 = 3
    . . .  3 = 6
   . . . .  4 = 10
   etc...
 Info:
  - https://en.wikipedia.org/wiki/Triangular_number
]]--


function triangle_numbers(n)
  local sum = 0
  for i = 1, n do
    sum = sum + i
  end
  return sum
end


function main()
  local n = io.read("n")
  print(triangle_numbers(n))
end


main()
