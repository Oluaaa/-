def bounded_binary_search(nums, target, left=0, right=0):
    if left == 0 and right == 0:
        right = len(nums) - 1
    if left != 0 and right == 0:
        right = len(nums) - 1
    while left <= right:
        sred = left + (right - left) // 2
        elem = nums[sred]
        if elem == target:
            return sred
        if elem < target:
            left = sred + 1
        else:
            right = sred - 1
    return -1


print(bounded_binary_search([10, 20, 30, 40, 50], 40))

print(bounded_binary_search([10, 20, 30, 40, 50], 60, left=0, right=4))

print(bounded_binary_search([1, 3, 5, 7, 9], 5, 1, 3))

print(bounded_binary_search([1, 3, 5, 7, 9], 5, 0, 1))

print(bounded_binary_search([1], 1,left=0))

print(bounded_binary_search([-1, 0, 1], -1, right=1))
