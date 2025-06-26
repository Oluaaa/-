def move_zeros(nums: list):
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] == 0:
                nums.remove(0)
                nums.append(0)


nums = [0, 1, 2]
move_zeros(nums)
print(nums)

nums = [0, 2, 1]
move_zeros(nums)
print(nums)

nums = [1, 2, 3]
move_zeros(nums)
print(nums)

nums = [1]
move_zeros(nums)
print(nums)

nums = [1, 1, 1, 1]
move_zeros(nums)
print(nums)


nums = [0, 0, 0]
move_zeros(nums)
print(nums)
