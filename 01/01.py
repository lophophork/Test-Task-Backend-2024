def sort_array(array):
    for i in range(len(array)):
        low_id = i
        for j in range(i+1, len(array)):
            if array[j] < array[low_id]:
                low_id = j
        array[i], array[low_id] = array[low_id], array[i]
    return array

test_array = [21, 42, 11, 47, 4, 46, 2]
sort_array(test_array)
print(test_array)