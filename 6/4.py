def count_numbers(n, k):
    count = 0
    for i in range(1, n + 1):
        if i - sum([int(j) for j in str(i)]) >= k:
            count += 1
    return count

print(count_numbers(13, 2))    # 10, 11, 12, 13

print(count_numbers(10, 5))    # 10

print(count_numbers(1, 0))     # 1

print(count_numbers(10, 0))     # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print(count_numbers(10, 1))     # 10

print(count_numbers(10, 15))
