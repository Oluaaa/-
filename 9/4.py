def sort_like_nums(nums):
    n = len(nums)
    for i in range(n - 1):
        min_nums = i
        for j in range(i + 1, n):
            if type(nums[i]) is list and type(nums[j]) is list:
                if nums[i] > nums[j]:
                    min_nums = j
            elif type(nums[i]) is list and type(nums[j]) is int:
                if int(''.join([str(k) for k in nums[i]])) > nums[j]:
                    min_nums = i
                elif [k for k in nums[i]] == nums[j]:
                    min_nums = j
            elif type(nums[i]) is int and type(nums[j]) is list:
                if nums[i] > int(''.join([str(k) for k in nums[j]])):
                    min_nums = j
                elif [k for k in nums[j]] == nums[i]:
                    min_nums = i
            elif type(nums[i]) is int and type(nums[j]) is int:
                if nums[i] > nums[j]:
                    min_nums = j
                elif nums[i] == nums[j]:
                    min_nums = j
        nums[i], nums[min_nums] = nums[min_nums], nums[i]


nums = [[4], 3, 2, [5], [1]]
sort_like_nums(nums)
print(nums)


nums = [2, 1, [2], 3, [3]]
sort_like_nums(nums)
print(nums)

nums = [[1]]
sort_like_nums(nums)
print(nums)

nums = [[1], 1]
sort_like_nums(nums)
print(nums)

nums = [[4], [3], [2], [5], [1]]
sort_like_nums(nums)
print(nums)

nums = [-1, [-1], [-2], -2, [-1]]
sort_like_nums(nums)
print(nums)