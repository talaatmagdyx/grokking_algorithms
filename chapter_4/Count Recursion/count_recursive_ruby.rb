def count(arr)
  arr == [] ?  0 :  1 + count(arr[1..-1])
end

puts count([])
puts count([4])
puts count([4,2])