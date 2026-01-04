""" Sort Colors (0, 1, 2)

Algorithm:
1. Start
2. Count number of 0s, 1s, and 2s
3. Overwrite the array with 0s, then 1s, then 2s
4. End
"""

def sort_colors(nums):
    count_0 = nums.count(0)
    count_1 = nums.count(1)
    count_2 = nums.count(2)

    index = 0

    for _ in range(count_0):
        nums[index] = 0
        index += 1

    for _ in range(count_1):
        nums[index] = 1
        index += 1

    for _ in range(count_2):
        nums[index] = 2
        index += 1


# Example test
colors = [2, 0, 2, 1, 1, 0]
sort_colors(colors)
print(colors)
