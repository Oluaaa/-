from collections import Counter

def least_frequent_number(nums):
    count = Counter(nums)
    index = min(count.values())
    answer = max(nums)
    for num in count:
        if count[num] == index:
            if num < answer:
                answer = num

    return answer


print(least_frequent_number([4, 2, 4, 1, 3, 2, 1]))

print(least_frequent_number([3, 2, 1, 1, 3, 2, 1]))

print(least_frequent_number([1]))

print(least_frequent_number([1, 1, 1, 1, 1]))

print(least_frequent_number([1, 10, 100, 1000]))

print(least_frequent_number([1, 1, 10]))