def find_peaks(nums):
    count = 0
    for i in range(0, len(nums) - 1):
        if nums[i] < nums[i + 1] and i + 1 != len(nums) - 1:
            count += 1
    return count

print(find_peaks([16, 7, 18, 12, 13, 11, 19, 9, 10, 6]))    # 18, 13, 19 и 10

print(find_peaks([1, -1, 1, -2, 2, -2, -3, 3, -3]))          # 1, 2, 3

print(find_peaks([3, 1, 3]))

print(find_peaks([3, 1, 0]))

print(find_peaks([1, 3, 2]))                                # 3

print(find_peaks([1, 1, 1]))
