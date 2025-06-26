def cocktail_sort(nums: list):
    n = len(nums)
    flag = 'left'
    while nums != sorted(nums):
        for i in range(n - 1):
            if flag == 'left':
                for j in range(n - i - 1):
                    if nums[j] > nums[j + 1]:
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = 'right'
                # print(flag)
            else:
                for j in range(n - i - 1, -1, -1):
                    if nums[j] > nums[j + 1]:
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = 'left'
                # print(flag)


data = [8, 9, 6, 5, 7, 4, 1, 2, 3]
cocktail_sort(data)
print(data)

data = [5, 4, 3, -2, 1]
cocktail_sort(data)
print(data)

data = [3]
cocktail_sort(data)
print(data)

data = [1, 2, 3, 4, 5]
cocktail_sort(data)
print(data)

data = [2, 1]
cocktail_sort(data)
print(data)

data = [1, 1, 1, 1, 1]
cocktail_sort(data)
print(data)