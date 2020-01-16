const quicksort = arr => {
	if (arr.length < 2) return arr;
	const pivot = arr[0];
  let less = arr.slice(1).filter(function(i)  { return i <= pivot});
  let more = arr.slice(1).filter(function(i)  { return i > pivot});
  return quicksort(less).concat([pivot]).concat(quicksort(more));
};

console.log(quicksort([1,10,5,0,-1]));
