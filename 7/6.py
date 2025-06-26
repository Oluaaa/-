def max_to_min(nums):
    max_num = max(nums)
    min_num = min(nums)
    for i in range(len(nums)):
        if nums[i] == max_num:
            nums[i] = min_num



data = [1, 3, 3, 3, 4]
max_to_min(data)
print(data)
# [1, 3, 3, 3, 1]


data = [5, 4, 2, -2, 4, 2, 2, 5]
max_to_min(data)
print(data)
# [-2, 4, 2, -2, 4, 2, 2, -2]

data = [1]
max_to_min(data)
print(data)
# [1]


data = [1, 2, 1, 2, 1, 2]
max_to_min(data)
print(data)
# [1, 1, 1, 1, 1, 1]


data = [1, 1, 1, -1, 1, 1, 0]
max_to_min(data)
print(data)
# [-1, -1, -1, -1, -1, -1, 0]


data = [1, 1]
max_to_min(data)
print(data)
# [1, 1]