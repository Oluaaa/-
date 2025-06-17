def mystery(n):
    count = 0
    for i in str(n):
        if i == '0':
            count += 1
        if i == '9':
            count += 1
        if i == '8':
            count += 2
        if i == '6':
            count += 1
    return count


print(mystery(0))
print(mystery(1))
print(mystery(10))
print(mystery(18))