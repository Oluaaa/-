def section_sort(nums):
    n = len(nums)
    zero = 0
    for i in range(n):
        if nums[i] == 0:
            nums[zero:i] = sorted(nums[zero:i])
            zero = i + 1
    if zero < n:
        nums[zero:] = sorted(nums[zero:])


nums = [2, 1, 0, 3, 2, 1, 0]
section_sort(nums)
print(nums)

nums = [1, 1, 1, 0, 5, 3, 4, 0, 2, 5, 3, 0, 3, 2, 1, 0]
section_sort(nums)
print(nums)

nums = [1, 1, 1, 0, 2, 2, 2, 0]
section_sort(nums)
print(nums)

nums = [3, 2, 1, 0]
section_sort(nums)
print(nums)

nums = [1, 0]
section_sort(nums)
print(nums)

nums = [5, 4, 3, 0, 2, 1, 0]
section_sort(nums)
print(nums)
