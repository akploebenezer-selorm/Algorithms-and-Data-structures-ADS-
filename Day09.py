"""
 Palindrome Partitioning

Algorithm:
1. Use backtracking to explore partitions
2. Check if substring is palindrome
3. Store valid partitions
4. End
"""

def is_palindrome(s):
    return s == s[::-1]


def palindrome_partition(s):
    result = []

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return result


# Example test
text = "aab"
print(palindrome_partition(text))
