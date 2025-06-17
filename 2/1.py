def get_quadrant(p):
    if p[0] == 0 or p[1] == 0:
        return None
    elif p[0] > 0 and p[1] > 0:
        return 1
    elif p[0] < 0 < p[1]:
        return 2
    elif p[0] < 0 and p[1] < 0:
        return 3
    elif p[0] > 0 > p[1]:
        return 4



print(get_quadrant((3, 4)))

print(get_quadrant((-1, 2)))

print(get_quadrant((-3, -5)))

print(get_quadrant((1, -1)))

print(get_quadrant((5, 0)))

print(get_quadrant((0, 0)))
