def is_point_in_rectangle(p, rect): #(2, 2), [(1, 1), (3, 4)])
    if p[0] == rect[0][0] or p[0] == rect[1][0]:
        return False
    elif p[1] == rect[0][1] or p[1] == rect[1][1]:
        return False
    elif p[0] < rect[0][0] and p[0] < rect[1][0]:
        return False
    elif p[0] > rect[0][0] and p[0] > rect[1][0]:
        return False
    elif p[1] < rect[0][1] and p[1] < rect[1][1]:
        return False
    elif p[1] > rect[0][1] and p[1] > rect[1][1]:
        return False
    return True

print(is_point_in_rectangle((2, 2), [(1, 1), (3, 4)]))

print(is_point_in_rectangle((1, 0), [(1, 1), (3, 4)]))

print(is_point_in_rectangle((2, 1), [(1, 1), (3, 4)]))

print(is_point_in_rectangle((0, 0), [(-1, -1), (3, 3)]))

print(is_point_in_rectangle((3, 0), [(0, 0), (10, 1)]))

print(is_point_in_rectangle((-5, -6), [(-10, -7), (-4, -2)]))
