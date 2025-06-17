def avg_values(nums):
    lst_values = []
    lst_prevalues = []
    for num in nums:
        lst_prevalues.append(num)
        lst_values.append(sum(lst_prevalues) / len(lst_prevalues))

    return lst_values


print(avg_values([10, 20, 30, 40, 50]))
print(avg_values([1, 1, 1, 1, 1]))
print(avg_values([-2, -3, 5, 5]))
print(avg_values([]))
print(avg_values([0, 0, 0, 0]))
print(avg_values([3]))