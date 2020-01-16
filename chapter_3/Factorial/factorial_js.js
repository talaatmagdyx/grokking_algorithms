const fact = x => {
	return x === 1 ?  1 :  x * fact(x-1);
};

console.log(fact(3));