def count(arr):
	# 0 if arr == [] else (arr[0] + count (arr[1:])) can't work ?
	if arr == [] :
		return 0
	return 1 + count(arr[1:])

print( count([]) )
print( count([4]) )
print( count([4,2]) )