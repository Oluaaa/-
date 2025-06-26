def search_insert_position(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    nums.append(target)
    nums = sorted(nums)
    return(nums.index(target))

print(search_insert_position([1, 2, 3, 4, 5], 5))

print(search_insert_position([1, 2, 3, 4, 5], 6))

print(search_insert_position([1, 2, 4, 5], 3))

print(search_insert_position([2, 3, 4, 5, 6], 1))

print(search_insert_position([1], 2))

print(search_insert_position([1], 1))
