def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        item = nums[i]
        j = i - 1
        while j >= 0 and item > nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item


nums = [3, 4, 1, 2, 5]
insertion_sort(nums)
print(nums)

nums = [3, 2, 2, 1, 3, 3]
insertion_sort(nums)
print(nums)

nums = [1]
insertion_sort(nums)
print(nums)

nums = [5, 4, 3, 2, 1]
insertion_sort(nums)
print(nums)

nums = [-2, -10, -7, -6]
insertion_sort(nums)
print(nums)

nums = [-3, -3, -3, -3]
insertion_sort(nums)
print(nums)
