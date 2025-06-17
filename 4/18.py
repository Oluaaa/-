def divisible(n):
    count = 0
    for i in str(n):
        if i == '0':
            continue
        else:
            if n % int(i) == 0:
                count += 1
    return count

print(divisible(22))
print(divisible(500))
print(divisible(1))
print(divisible(11))
print(divisible(2340))
print(divisible(23))