def max_guests(n, m):
    return (n - 1) * m * 3

print(max_guests(5, 10))
#120
print(max_guests(10, 10))
#270
print(max_guests(2, 5))
#15
print(max_guests(1, 5))
#0
print(max_guests(2, 1))
#3
print(max_guests(1, 1))
#0