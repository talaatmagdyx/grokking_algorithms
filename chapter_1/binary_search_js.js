const binary_search = (list, target_search, low = 0 ,high = list.length) => {
    while (low <= high){
        let mid = (low + high) / 2;
        let guess = list[mid];
        if (guess === target_search){
            return mid
        }else if (guess < target_search){
            low = mid + 1;
        }else{
            high = mid -1;
        }
    }
    return false;
};

my_list = [1,2,5,6,7,10,16];
console.log(binary_search(my_list,10));