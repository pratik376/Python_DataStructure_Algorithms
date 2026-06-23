def subArraySum(arr):

    MOD = 10**9 + 7
    res = 0

    arr = [float('-inf')] + arr + [float('-inf')]
    stack = []   # (index, value)

    for i, n in enumerate(arr):

        while stack and n < stack[-1][1]:

            j, m = stack.pop()

            left = j - stack[-1][0]
            right = i - j

            res = (res + m * left * right) % MOD

        stack.append((i, n))

    return res