def sort_by_digit_and_value(nums: list):
    n = len(nums)
    for i in range(n - 1):
        min_nums = i
        for j in range(i + 1, n):
            if str(nums[j])[-1] > str(nums[min_nums])[-1]:
                min_nums = j
            elif str(nums[j])[-1] == str(nums[min_nums])[-1] and nums[j] < nums[min_nums]:
                min_nums = j
        nums[i], nums[min_nums] = nums[min_nums], nums[i]



nums = [5, 11, 183, 19, 274]
sort_by_digit_and_value(nums)
print(nums)

nums = [5, 11, 185, 19, 271]
sort_by_digit_and_value(nums)
print(nums)

nums = [1]
sort_by_digit_and_value(nums)
print(nums)

nums = [11111, 1111, 111, 11, 1]
sort_by_digit_and_value(nums)
print(nums)

nums = [11, 12, 13, 14, 15]
sort_by_digit_and_value(nums)
print(nums)

nums = [6, -2, 7, 2, -6]
sort_by_digit_and_value(nums)
print(nums)