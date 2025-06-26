def max_sum_of_k_elements(nums, k):
    return sum(sorted(nums)[-k:])

print(max_sum_of_k_elements([4, 2, 3, 1], 2))

print(max_sum_of_k_elements([-2, 4, 0, -3], 2))

print(max_sum_of_k_elements([1], 1))

print(max_sum_of_k_elements([-1, 1, -1, 1], 4))

print(max_sum_of_k_elements([-1, -2, -3], 3))

print(max_sum_of_k_elements([0, 2, 4, 6], 1))
