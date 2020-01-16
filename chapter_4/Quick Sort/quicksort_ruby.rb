def quicksort(arr)
  return arr if arr.length < 2
  pivot = arr[0]
  less = arr[1..-1].select{|num| num<=pivot}
  # can use (arr[1..-1]-less[0..-1]) return same result
  more = arr[1..-1].select{|num| num >pivot}

  return quicksort(less) + [pivot] + quicksort(more)
end

print quicksort([11,12,13,0,1,5,-1,11])
