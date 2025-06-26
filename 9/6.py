def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break


nums = [3, 4, 1, 2, 5]
bubble_sort(nums)
print(nums)

nums = [3, 2, 2, 1, 3, 3]
bubble_sort(nums)
print(nums)

nums = [1]
bubble_sort(nums)
print(nums)

nums = [5, 4, 3, 2, 1]
bubble_sort(nums)
print(nums)

nums = [-2, -10, -7, -6]
bubble_sort(nums)
print(nums)

nums = [-3, -3, -3, -3]
bubble_sort(nums)
print(nums)
