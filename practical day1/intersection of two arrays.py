def intersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1 & set2)
arr1 = [1, 2, 2, 1]
arr2 = [2, 2, 3]
result = intersection(arr1, arr2)
print(result)  
