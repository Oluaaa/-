def mystery(n):
    fin = 0
    for i in range(1, n + 1):
        fin += i
    return fin

print(mystery(1))
print(mystery(2))
print(mystery(3))
print(mystery(4))
