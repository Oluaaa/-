def training_time(n, m, s, d):
    return ((m * 60 + s) * n + (n - 1) * d) // 60, ((m * 60 + s) * n + (n - 1) * d) % 60

print(training_time(3, 2, 10, 90))
#(9, 30)
print(training_time(1, 1, 0, 0))
#(1, 0)
print(training_time(1, 0, 1, 0))
#(0, 1)
print(training_time(1, 1, 1, 1))
#(1, 1)
print(training_time(2, 1, 1, 0))
#(2, 2)
print(training_time(1, 1, 0, 1))
#(1, 0)