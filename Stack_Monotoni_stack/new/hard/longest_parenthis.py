def longest_parentheses(s):

    stack = []  # (index, value)

    for index in range(len(s)):

        if s[index] == ")" and stack and s[stack[-1]] == "(":
            stack.pop()
        else:
            stack.append(index)

    index = -1
    max_val = 0

    for i in stack:

        max_val = max(max_val, i - index - 1)
        index = i

    max_val = max(max_val, len(s) - index - 1)

    return max_val
