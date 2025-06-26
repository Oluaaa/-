from collections import Counter

def count_triplet_numbers(nums):
    count = Counter(nums)
    index = 0
    for num in count:
        if count[num] == 3:
            index += 1
    return index


print(count_triplet_numbers([4, 5, 6, 4, 5, 4, 5, 6]))

print(count_triplet_numbers([5, 4, 5, 5, 4, 5, 7, 4]))

print(count_triplet_numbers([4, 5, 4, 6, 5, 7, 5, 5]))

print(count_triplet_numbers([5]))

print(count_triplet_numbers([1, 1, 1, 1]))

print(count_triplet_numbers([7, 7, 7]))
