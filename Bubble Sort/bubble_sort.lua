--[[
  Jacobus Burger (2025-09-24)
  Bubble Sort (Lua 5.4)
  Bubble Sort is a straightforwards sorting algorithm and often the first
    taught in Compting Science courses. It's time complexity of O(n^2)
    is "bad" on large arrays, but it's simple design makes it
    straightforward to implement and effective to use on smaller
    arrays. Overall, it's a decent if inefficient sorting algorithm!
  see:
  - https://en.wikipedia.org/wiki/Bubble_sort
  - https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort#Lua
]]


local function sort(array)
  for _ = 1, #array do
    for i = 2, #array do
      if array[i - 1] > array[i] then
        array[i - 1], array[i] = array[i], array[i - 1]
      end
    end
  end
end


local function main()
  -- get input
  local n = io.read("n")
  -- sadly, no comprehensions in moonlang 🌕 like in snakelang 🐍
  math.randomseed(os.time())
  local array = {}
  for _ = 1, n do
    table.insert(array, math.random(n))
  end

  -- show unsorted
  -- moonlang 🌕 does have nice features like table.concat
  print(table.concat(array, ' '))

  -- sort
  sort(array)

  -- show sorted
  print(table.concat(array, ' '))
end


main()
