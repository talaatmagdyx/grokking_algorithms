def sum(arr):
	# 0 if arr == [] else (arr[0] + sum (arr[1:])) can't work ?
	if arr == [] :
		return 0
	return arr[0] + sum(arr[1:])

print( sum([]) )
print( sum([4]) )
print( sum([4,2]) )