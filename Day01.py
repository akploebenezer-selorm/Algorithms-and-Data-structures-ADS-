"""

Algorithm:
1. Start
2. Create an empty dictionary to store numbers and their indices
3. Loop through the array
4. For each number, calculate target - number
5. If the result exists in the dictionary, return the two indices
6. Otherwise, store the number and its index
7. End
"""

def two_sum(nums, target):
    seen = {}

    for index, value in enumerate(nums):
        required = target - value

        if required in seen:
            return seen[required], index

        seen[value] = index


# Example 
numbers = [2, 7, 11, 15]
target = 9

print(two_sum(numbers, target))
