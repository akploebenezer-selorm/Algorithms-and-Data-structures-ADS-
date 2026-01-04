"""
  Permutation within String

Algorithm:
1. If s1 is longer than s2, return False
2. Count character frequency of s1
3. Use sliding window on s2 with same length as s1
4. Compare window frequency with s1 frequency
5. Return True if match is found, else False
"""

def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    freq1 = {}
    freq2 = {}

    # Count frequency of s1
    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1

    window_size = len(s1)

    # First window
    for i in range(window_size):
        freq2[s2[i]] = freq2.get(s2[i], 0) + 1

    if freq1 == freq2:
        return True

    # Slide the window
    for i in range(window_size, len(s2)):
        start_char = s2[i - window_size]
        freq2[start_char] -= 1
        if freq2[start_char] == 0:
            del freq2[start_char]

        freq2[s2[i]] = freq2.get(s2[i], 0) + 1

        if freq1 == freq2:
            return True

    return False


# Example test
s1 = "ab"
s2 = "eidbaooo"
print(check_inclusion(s1, s2))
