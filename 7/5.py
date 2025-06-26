def can_nest(nums1, nums2):
    if min(nums1) > min(nums2) and max(nums1) < max(nums2):
        return True
    if min(nums2) > min(nums1) and max(nums2) < max(nums1):
        return True
    return False


print(can_nest([1, 2, 3, 4], [0, 6]))     # первый список можно вложить во второй

print(can_nest([4, 0], [3, 1]))           # второй список можно вложить в первый

print(can_nest([1, 2, 3, 4], [2, 3]))     # второй список можно вложить в первый

print(can_nest([9, 9, 8], [8, 9]))        # минимумы и максимумы списков совпадают

print(can_nest([1], [1]))                 # минимумы и максимумы списков совпадают

print(can_nest([-1, 1, -2], [-3, 2, 0]))  # первый список можно вложить во второй
