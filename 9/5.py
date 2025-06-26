def alter_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        min_nums = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_nums]:
                min_nums = j
        nums[i], nums[min_nums] = nums[min_nums], nums[i]
    lst = []
    left, right = 0, len(nums) - 1
    while left <= right:
        if right >= left:
            lst.append(nums[right])
            right -= 1
        if left <= right:
            lst.append(nums[left])
            left += 1
    for i in range(n):
        nums[i] = lst[i]


nums = [1, 2, 3, 4, 5]
alter_sort(nums)
print(nums)

nums = [5, 4, 3, 2, 1]
alter_sort(nums)
print(nums)

nums = [1, 1, 1]
alter_sort(nums)
print(nums)

nums = [2, 3, 1, 5, 5, 3, 1]
alter_sort(nums)
print(nums)

nums = [-1, -5, -3, -2, -7, -4]
alter_sort(nums)
print(nums)

nums = [2]
alter_sort(nums)
print(nums)