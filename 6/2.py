def equal(nums):
    for i in range(len(nums)):
        if i == nums[i]:
            return i
    return -1

print(equal([10, 7, 2]))

print(equal([2, 1, 4, 3]))

print(equal([2, 9, 4, 8]))

print(equal([0]))

print(equal([0, 1, 2, 3]))

print(equal([]))
