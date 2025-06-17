def swap_digits(n):
    n3 = n % 10 % 10
    n2 = n // 10 % 10
    n1 = n // 100
    finish = n3 * 100 + n2 * 10 + n1
    return finish

print(swap_digits(123))
#321
print(swap_digits(321))
#123
print(swap_digits(555))
#555
print(swap_digits(545))
#545
print(swap_digits(550))
#55
print(swap_digits(500))
#5