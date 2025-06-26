def sum_of_seven_smallest(nums):
    n = len(nums)
    count = 0
    for i in range(n - 1):
        min_nums = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_nums]:
                min_nums = j
        nums[i], nums[min_nums] = nums[min_nums], nums[i]
    for i in range(7):
        count += nums[i]
    return count


print(sum_of_seven_smallest([2, 7, 3, 6, 10, 4, 1, 9, 5, 8]))    # 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
print(sum_of_seven_smallest([2, 2, 4, 1, 3, 3, 5, 4, 4]))        # 1 + 2 + 2 + 3 + 3 + 4 + 4 = 19
print(sum_of_seven_smallest([1, 1, 1, 1, 1, 1, 1, 1]))           # 1 + 1 + 1 + 1 + 1 + 1 + 1 = 7
print(sum_of_seven_smallest([-1, 1, -1, 1, -1, 1, -1, 1]))       # -1 - 1 - 1 - 1 + 1 + 1 + 1 = -1
print(sum_of_seven_smallest([-50, 15, 15, 20, 10, 15, 3, 2, 5])) # -50 + 2 + 3 + 10 + 15 + 15 + 15 = 0
print(sum_of_seven_smallest([-7, -2, -2, -8, -1, -4, -10]))      # -10 - 8 - 7 - 4 - 2 - 2 - 1 = -34