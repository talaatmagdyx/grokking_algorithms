def find_smallest(arr,n = arr.length)
  smallest = arr[0]
  smallest_index = 0

  (1..(n-1)).each do  |item| 

      if arr[item] < smallest
       smallest = arr[item]
       smallest_index = item
      end

  end
  return smallest_index
end


def selection_sort(list)

  new_list = []

  list.length.times do |item|
    smallest = find_smallest(list)
    new_list.push(list.delete_at(smallest))
  end

  return new_list

end

puts selection_sort([1,3,4,0,-1])
