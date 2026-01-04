""" Maximum Subarray Sum

Algorithm:
1. Start
2. Initialize max_sum with the first element
3. Initialize current_sum as 0
4. Loop through the array
5. Add each element to current_sum
6. Update max_sum if current_sum is larger
7. Reset current_sum to 0 if it becomes negative
8. Return max_sum
9. End
"""

def max_subarray_sum(nums):
    max_sum = nums[0]
    current_sum = 0

    for num in nums:
        current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0

    return max_sum


# Example 
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(numbers))
