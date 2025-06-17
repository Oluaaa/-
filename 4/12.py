def sum_of_squares(n):
    return sum([i ** 2 for i in range(1, n + 1)])

print(sum_of_squares(1))    # 1

print(sum_of_squares(2))    # 1 + 4 = 5

print(sum_of_squares(3))    # 1 + 4 + 9 = 14

print(sum_of_squares(5))    # 1 + 4 + 9 + 16 + 25 = 55
