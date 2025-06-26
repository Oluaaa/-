def number_of_swaps(nums):
    n = len(nums)
    count = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                count += 1
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return count


print(number_of_swaps([1, 2, 4, 3, 5]))

print(number_of_swaps([2, 1, 4, 3, 5]))

print(number_of_swaps([1, 2, 3, 4, 5]))

print(number_of_swaps([5, 4, 3, 2, 1]))

print(number_of_swaps([1]))

print(number_of_swaps([2, 1]))
