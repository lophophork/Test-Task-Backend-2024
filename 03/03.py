def sum_max(array):
    max_ar = array[0]
    second_max_ar = None
    
    for ar in array[1:]:
        if ar > max_ar:
            second_max_ar = max_ar
            max_ar = ar
        elif second_max_ar is None or ar > second_max_ar:
            second_max_ar = ar

    max_sum = max_ar + second_max_ar
    return max_sum

nums = [2, 7, 4, 1, 8]
result = sum_max(nums)
print(f'Наибольшая сумма двух чисел в списке: {result}')