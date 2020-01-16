def count_down(x)
	puts (x)
	if x <= 0 
		return 
	else
		count_down( x-1 )
	end
end

count_down(3)