def binary_search(array, x):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1

nums = [2, 4, 5, 7, 9, 11, 10, 15, 20, 27]
element = 11
result = binary_search(nums, element)
print(f'Индекс элемента {element}: {result}')