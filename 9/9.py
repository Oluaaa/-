def k_swaps_to_sort(n, k):
    result = []
    inv_remaining = k
    for i in range(1, n + 1):
        current_length = len(result)
        x = min(inv_remaining, current_length)
        pos = current_length - x
        result.insert(pos, i)
        inv_remaining -= x
    return result


print((k_swaps_to_sort(5, 3)))

print((k_swaps_to_sort(5, 3)))

print((k_swaps_to_sort(1, 0)))

print((k_swaps_to_sort(5, 1)))

print((k_swaps_to_sort(5, 10)))

print((k_swaps_to_sort(7, 4)))

print((k_swaps_to_sort(10, 45)))
