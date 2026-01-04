"""
 Minimum Window Substring

Algorithm:
1. Count frequency of characters in t
2. Use sliding window on s
3. Expand window until all characters are included
4. Shrink window to find minimum length
5. Return the smallest valid substring
"""

def min_window(s, t):
    if not s or not t:
        return ""

    need = {}
    for char in t:
        need[char] = need.get(char, 0) + 1

    have = {}
    required = len(need)
    formed = 0

    left = 0
    min_len = float("inf")
    min_window = ""

    for right in range(len(s)):
        char = s[right]
        have[char] = have.get(char, 0) + 1

        if char in need and have[char] == need[char]:
            formed += 1

        while formed == required:
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                min_window = s[left:right + 1]

            left_char = s[left]
            have[left_char] -= 1
            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1

            left += 1

    return min_window


# Example test
s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))
