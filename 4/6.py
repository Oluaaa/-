def drop_one_and_five(n):
    count = 0
    n1 = 0
    nuit = 1
    while n > 0:
        n1 = n % 10
        n = n // 10

        if n1 != 1 and n1 != 5:
            count += n1 * nuit
            nuit *= 10
    return count

print(drop_one_and_five(527012)) #2702
print(drop_one_and_five(2468)) #2468
print(drop_one_and_five(0)) #0
print(drop_one_and_five(1155)) #0
print(drop_one_and_five(10)) #0
print(drop_one_and_five(105)) #0