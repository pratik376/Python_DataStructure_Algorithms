def dfs(start):

    for i in range(start, len(nums)):

        path.append(nums[i])

        dfs(i + 1)

        path.pop()