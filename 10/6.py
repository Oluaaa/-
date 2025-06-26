from collections import Counter

def count_beautiful_pairs(nums):
    count = Counter(nums)
    answer = 0
    for num in count:
        answer += count[num] // 2
    return answer

## решение с счётчиком. Находится пара -> +1 счётчик, после его сброс на 2 т.к для Counter находит число вхождение числа "n" = 2.

# from collections import Counter
#
# def count_beautiful_pairs(nums):
#     count = Counter(nums)
#     answer = 0
#     for num in count:
#         c = 0
#         while count[num] >= 2:
#             c += 1
#             count[num] -= 2
#         answer += c
#     return answer


print(count_beautiful_pairs([1, 4, 5, 4, 1, 1, 0]))

print(count_beautiful_pairs([4, 4, 4, 4, 4, 4, 4]))

print(count_beautiful_pairs([1, 2, 3, 4, 5, 6, 7]))

print(count_beautiful_pairs([0, 0]))

print(count_beautiful_pairs([1, 1, 1]))

print(count_beautiful_pairs([0, 9, 9, 0]))
