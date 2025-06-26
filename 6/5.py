def nine_divisors(n):
    count = 0
    tot = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 9:
            tot += 1
            count = 0
        else:
            count = 0
    return tot

print(nine_divisors(100))     # 36, 100

print(nine_divisors(10))

print(nine_divisors(50))     # 36
print(nine_divisors(300))    # 36, 100, 196, 225, 256

print(nine_divisors(500))    # 36, 100, 196, 225, 256, 441, 484

print(nine_divisors(1000))   # 36, 100, 196, 225, 256, 441, 484, 676
