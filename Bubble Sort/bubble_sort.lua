

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
  math.randomseed(os.time())
  local n = io.read("n")
  local array = {}
  for _ = 1, n do
    table.insert(array, math.random(n))
  end

  -- show unsorted
  for i = 1, n do
    io.write(string.format("%i ", array[i]))
  end
  print()

  -- sort
  sort(array)

  -- show sorted
  for i = 1, n do
    io.write(string.format("%i ", array[i]))
  end
  print()
end


main()
