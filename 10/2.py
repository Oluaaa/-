def binary_insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        for j in range(i, left, -1):
            nums[j] = nums[j - 1]
        nums[left] = key


nums = [3, 4, 1, 2, 5]
binary_insertion_sort(nums)
print(nums)

nums = [3, 2, 2, 1, 3, 3]
binary_insertion_sort(nums)
print(nums)

nums = [1]
binary_insertion_sort(nums)
print(nums)

nums = [5, 4, 3, 2, 1]
binary_insertion_sort(nums)
print(nums)

nums = [-2, -10, -7, -6]
binary_insertion_sort(nums)
print(nums)

nums = [-3, -3, -3, -3]
binary_insertion_sort(nums)
print(nums)