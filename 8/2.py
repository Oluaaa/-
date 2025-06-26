def binary_search(data, target):
    left = 0
    right = len(data) - 1
    while left <= right:
        sred = left + (right - left) // 2
        elem = data[sred]
        if elem == target:
            return sred
        if elem > target:
            left = sred + 1
        else:
            right = sred - 1
    return -1

print(binary_search([50, 40, 30, 20, 10], 30))

print(binary_search([50, 40, 30, 20, 10], 0))

print(binary_search([5, 4, 3, 2, 1], 5))

print(binary_search([5], 5))

print(binary_search([1, 0, -1], -1))

print(binary_search([5, 4, 3, 2, 1], 1))