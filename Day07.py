"""
 Sorting Characters by Frequency

Algorithm:
1. Count frequency of each character
2. Sort characters by frequency (descending)
3. Build result string
4. End
"""

def frequency_sort(s):
    freq = {}

    # Count frequency
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Sort characters by frequency
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Build result string
    result = []
    for char, count in sorted_chars:
        result.append(char * count)

    return "".join(result)


# Example test
text = "tree"
print(frequency_sort(text))
