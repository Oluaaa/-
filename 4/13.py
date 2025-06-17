def even_odd(nums):
    count1 = 0
    count2 = 0
    for i in nums:
        if i % 2 == 0:
            count1 += 1
        if i % 2 == 1:
            count2 += 1

    if count1 == len(nums):
        return True
    if count2 == len(nums):
        return True
    return False

print(even_odd([1, 3, 5, 7]))
print(even_odd([-2, 4, -6, 8]))
print(even_odd([1, 3, 4]))
print(even_odd([0, 0, 0]))
print(even_odd([1]))
print(even_odd([10, 0]))