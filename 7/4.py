def min_max_diff(nums):
    max_zn = 0
    min_zn = sum(nums)
    for i in nums:
        if i > max_zn:
            max_zn = i
        if i < min_zn:
            min_zn = i
    return max_zn - min_zn


print(min_max_diff([4, 5, 3, 2, 1]))  # 5 - 1 = 4

print(min_max_diff([5, 5, 5, 5, 5]))      # 5 - 5 = 0

print(min_max_diff([1, 2]))               # 2 - 1 = 1

print(min_max_diff([10, 10]))             # 10 - 10 = 0

print(min_max_diff([1]))                  # 1 - 1 = 0

print(min_max_diff([-10, -5, 0, 5, 10]))  # 10 - (-10) = 20
