def max (arr)
	return arr[0] if arr.length == 1 
	m = max(arr[1..-1])
	m >= arr[0] ?  m :  arr[0]
end

puts max([2,3,4])