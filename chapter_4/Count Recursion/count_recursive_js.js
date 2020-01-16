const count  = arr => arr.length === 0 ? 0 : 1 + count(arr.slice(1));



console.log( count([]) );
console.log( count([4]) );
console.log( count([4,2]) );