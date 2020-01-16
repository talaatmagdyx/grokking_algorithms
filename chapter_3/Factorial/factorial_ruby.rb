def fact(x)
	return	x == 1 ? 1 : x * fact(x-1);
end

puts (fact(3))