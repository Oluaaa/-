def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        min_nums = i
        for j in range(i + 1, n):
            if nums[j] > nums[min_nums]:
                min_nums = j
        nums[i], nums[min_nums] = nums[min_nums], nums[i]


nums = [3, 4, 1, 2, 5]
selection_sort(nums)
print(nums)

nums = [3, 2, 2, 1, 3, 3]
selection_sort(nums)
print(nums)

nums = [1]
selection_sort(nums)
print(nums)

nums = [5, 4, 3, 2, 1]
selection_sort(nums)
print(nums)

nums = [-2, -10, -7, -6]
selection_sort(nums)
print(nums)

nums = [-3, -3, -3, -3]
selection_sort(nums)
print(nums)