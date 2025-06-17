def min_digit_sum(a, b):
    slov = {}
    counter = 0
    # for i in range(a, b + 1):
    #     slov[i] = sum([int(j) for j in str(i)])
    # min_slov = min(slov)
    # for k, v in slov.items():
    #
    #     if v == min_slov:
    #         counter += 1
    # return min_slov

    for i in range(a, b + 1):
        if len(str(i)) == 1:
            slov[i] = i
        else:
            slov[i] = sum([int(j) for j in str(i)])
        min_sum = min(slov.values())
    for key, values in slov.items():
        if values == min_sum:
            counter += 1
    return counter


print(min_digit_sum(1, 50))
print(min_digit_sum(1, 100))
print(min_digit_sum(50, 200))
print(min_digit_sum(1, 1))
print(min_digit_sum(1, 1000))
print(min_digit_sum(456, 678))



# {1: 1; 02:2...10: 1.. 49: 13; 50: 5}
# for k, v in slovar:
#     if v == min(slovar):
#         counter += 1