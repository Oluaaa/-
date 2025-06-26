def min_product_of_two(nums):
    min_sum = sum(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] * nums[j] < min_sum:
                min_sum = nums[i] * nums[j]
    return min_sum


print(min_product_of_two([5, 2, 6, 1, 7]))

print(min_product_of_two([1, 1, 1, 1, 1]))

print(min_product_of_two([5, 4, 3, 2, 1]))

print(min_product_of_two([1, 5, 4, 3, 2]))

print(min_product_of_two([1, 2, 1, 3, 4]))

print(min_product_of_two([3, 4, 5, 2, 2]))