def mystery(n):
    if n % 2 == 1:
        return n + 1
    return n + 2

print(mystery(1))
#2
print(mystery(2))
#4
print(mystery(3))
#4
print(mystery(4))
#6
print(mystery(5))
#6
print(mystery(0))
#2
print(mystery(10))
#12
print(mystery(100))
#102
print(mystery(1000))
#1002
print(mystery(999))
#1000