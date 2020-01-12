def binary_search(list, target_search, low=0, high=len(list)-1):
    while low <= high :
        mid = (low + high) // 2
        guess = list[mid]
        if guess == target_search:
            return mid
        elif guess < target_search:
            low = mid + 1
        else:
            high = mid -1

    return False

mylist = [1,2,3,4,5,6,7]
print(binary_search(mylist, 4))