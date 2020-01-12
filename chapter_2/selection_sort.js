const find_smallest = (arr,n = arr.length) => {
  let smallest = arr[0] ;
  let smallest_index = 0;
  for (let i = 1; i < n; i++){
    if(arr[i] < smallest){
      smallest = arr[i] ;
      smallest_index = i ;
    }
  }
  return smallest_index;
};


const selection_sort = (list) => {
  let  new_list = [] ;
  let  length = list.length;
  for (let i = 0; i < length; i++){
    console.log(i);
    let smallest = find_smallest(list);
    new_list.push(list.splice(smallest, 1)[0]);
    console.log("Hello" + i);

  }
  
  return new_list;
};


console.log(selection_sort([1,3,4,0,-1]));