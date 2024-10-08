def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        if target - num in num_map:
            return [num_map[target - num], i]
        num_map[num] = i
    return []
print(two_sum([2, 7, 11, 15], 9))
