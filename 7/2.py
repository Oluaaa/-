def max_of_four(a, b, c, d):
    if d >= a and d >= b and d >= c:
        return d
    if a >= c and a >= d and a >= b:
        return a
    if b >= d and b >= c and b >= a:
        return b
    if c >= a and c >= b and c >= d:
        return c

print(max_of_four(4, 9, 10, 5))

print(max_of_four(5, 5, 5, 5))

print(max_of_four(0, -1, -1, 0))

print(max_of_four(-3, -5, -1, -2))

print(max_of_four(1, -2, -1, 2))

print(max_of_four(10, 1, 1, 1))
