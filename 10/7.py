def sort_binary_list(binary_list):
    answer = 0
    for num in binary_list:
        if num == 0:
            answer += 1

    binary_list[::] = [0] * answer + [1] * (len(binary_list) - answer)


binary_list = [0, 1, 1, 0, 1]
sort_binary_list(binary_list)
print(binary_list)

binary_list = [0, 0, 0, 0, 0]
sort_binary_list(binary_list)
print(binary_list)

binary_list = [1, 1, 1, 1, 1]
sort_binary_list(binary_list)
print(binary_list)

binary_list = [1]
sort_binary_list(binary_list)
print(binary_list)

binary_list = [0, 1]
sort_binary_list(binary_list)
print(binary_list)

binary_list = [0, 1, 0, 1]
sort_binary_list(binary_list)
print(binary_list)
