# def third_max_value(nums):
#     lst = []
#     max_num = min(nums)
#     while len(lst) != 3:
#         for i in range(len(nums)):
#             if nums[i] > max_num:
#                 max_num = nums[i]
#         lst.append(max_num)
#         del nums[nums.index(max_num)]
#         max_num = -100000
#     return min(lst)

def third_max_value(nums):
    nums = sorted(nums)
    return nums[-3]

print(third_max_value([4, 8, 6, 10]))

print(third_max_value([4, 4, 4, 4]))

print(third_max_value([1, 2, 3]))

print(third_max_value([3, 2, 1]))

print(third_max_value([-1, -2, -3]))

print(third_max_value([4, 4, 2, 2, 1, 3, 5, 6]))
