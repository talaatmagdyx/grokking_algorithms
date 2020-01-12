def binary_search(list, target_search, low = 0, high = list.length - 1)
  while low <= high
    mid = (low + high) / 2
    guess = list[mid]
    if guess == target_search
      return mid
    elsif guess < target_search
      low = mid + 1
    else
      high = mid - 1
    end
  end
  nil
end

my_list = [1, 10, 15, 21, 30]
p binary_search(my_list, -1) # if use puts must use inspect
my_list = [1, 10, 15, 21, 30]
puts binary_search(my_list, 21)
my_list = [31, 20, 15, 2, 1]
p binary_search(my_list, 1)