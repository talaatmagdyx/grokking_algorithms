def sum(arr)
  arr == [] ?  0 :  arr[0] + sum(arr[1..-1])
end

puts sum([])
puts sum([4])
puts sum([4,2])