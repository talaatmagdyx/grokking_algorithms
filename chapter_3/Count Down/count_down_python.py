def count_down(i):
	print(i)
	if i <= 0 :
		return "Finished"
	else:
		count_down(i-1)
	
print(count_down(3))