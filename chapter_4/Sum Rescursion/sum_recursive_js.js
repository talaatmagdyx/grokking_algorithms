const sum  = arr => arr.length === 0 ? 0 : arr[0] + sum(arr.slice(1));



console.log( sum([]) );
console.log( sum([4]) );
console.log( sum([4,2]) );