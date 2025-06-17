def mid_num(a, b, c):
    lst = [a, b, c]
    max1 = max(a, b, c)
    min1 = min(a, b, c)
    lst.remove(max1)
    lst.remove(min1)
    return lst[0]


print(mid_num(1, 2, 3))  #2
print(mid_num(3, 1, 2))  #2
print(mid_num(-2, -3, -1))  #-2
print(mid_num(7, 7, 7))  #7
print(mid_num(0, 0, 0))  #0
print(mid_num(0, 0, 1))  #0
