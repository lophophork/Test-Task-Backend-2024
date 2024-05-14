def sort_array(A, B):
    result = []
    for b in B:
        for a in A:
            if a == b:
                result.append(a)
    
    not_b = [x for x in A if x not in B]
    
    for i in range(len(not_b)):
        for j in range(i + 1, len(not_b)):
            if not_b[i] < not_b[j]:
                not_b[i], not_b[j] = not_b[j], not_b[i]
                
    result.extend(not_b)
    return result

A = [2, 4, 1, 3, 2, 4, 6, 7, 9, 2, 19]
B = [2, 1, 4, 3, 6, 9]
sorted_array = sort_array(A, B)
print(f'Отсортированный массив A: {sorted_array}')