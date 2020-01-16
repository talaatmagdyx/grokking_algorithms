const max = arr => {
  if (arr.length == 1) return arr[0] ;
	let m = max(arr.slice(1));
	return m > arr[0] ? m : arr[0] ;
}

console.log(max([2,3,5]));