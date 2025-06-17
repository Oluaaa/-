def time_zone(h, a, b):
    if h - a < 0:
        if 24 - (h - a) + b > 23:
            return 24 - (h - a) + b - 24
        else:
            return 24 - (h - a) + b
    else:
        if h - a + b > 23:
            return h - a + b - 24
    return h - a + b

print(time_zone(12, 3, 7))
#16
print(time_zone(12, -4, 4))
#20
print(time_zone(12, 0, 0))
#12
print(time_zone(0, 0, 0))
#0
print(time_zone(6, -11, 12))
#5
print(time_zone(23, 12, -11))
#0