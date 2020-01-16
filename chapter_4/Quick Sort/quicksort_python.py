def quicksort(arr) :
  if len(arr) < 2: return arr 
  pivot = arr[0]
  less = [x for x in arr[1:] if x <= pivot]
  # can use list(set(arr(1:)) - set(less(1:))) same result
  more = [x for x in arr[1:] if x > pivot]

  return quicksort(less) + [pivot] + quicksort(more)


print (quicksort([11,12,13,0,1,5,-1]))
