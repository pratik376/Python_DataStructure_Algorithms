def dfs():
    if len(path) == len(nums):
        ans.append(path.copy())
        return

    for i in range(len(nums)):
        if used[i]:
            continue

        used[i] = True
        path.append(nums[i])

        dfs()

        path.pop()
        used[i] = False
"""
Subsets / Combinations:
After choosing index i
→ generally move forward
→ dfs(i + 1)

Permutations:
After choosing nums[i]
→ next choice can be ANY element
→ as long as it hasn't already been used

"""