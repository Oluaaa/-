def linear_search(nums, target, reverse=False):
    if len(nums) != 0:
        if reverse is False:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
            return -1
        if reverse is True:
            for i in range(len(nums) - 1, 0, -1):
                if nums[i] == target:
                    return i
            return -1
    else:
        return -1

print(linear_search([1, 5, 7], 5))


print(linear_search([2, 1, 7, 2], 2))

print(linear_search([12, 4, 1], 9))

print(linear_search([], 0))

print(linear_search([-2, 1, 7, -2], -2, reverse=True))

print(linear_search([1], 1))
