def golden_pairs(pairs):
    count = 0
    for i in pairs:
        if 1.7 >= max(i) / min(i) >= 1.6:
            count += 1
    return count


print(golden_pairs([(100, 165), (180, 100), (170, 100), (100, 160)]))

print(golden_pairs([(1, 10), (10, 1), (2, 5), (7, 4)]))

print(golden_pairs([(1, 1), (2, 2), (3, 3), (4, 4)]))

print(golden_pairs([(8, 5)]))

print(golden_pairs([(7, 4), (7, 5), (6, 7)]))

print(golden_pairs([(8, 5), (17, 10), (32, 20), (34, 20)]))
