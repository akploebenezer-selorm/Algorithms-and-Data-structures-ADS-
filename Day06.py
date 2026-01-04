"""
 Minimum Remove to Make Valid Parentheses

Algorithm:
1. Use a stack to track '(' positions
2. Mark invalid ')' and extra '('
3. Remove marked characters
4. Return valid string
"""

def min_remove_to_make_valid(s):
    stack = []
    s_list = list(s)
    remove = set()

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                remove.add(i)

    # Remaining '(' in stack are invalid
    for index in stack:
        remove.add(index)

    # Build result
    result = []
    for i, char in enumerate(s_list):
        if i not in remove:
            result.append(char)

    return "".join(result)


# Example test
text = "a)b(c)d"
print(min_remove_to_make_valid(text))
