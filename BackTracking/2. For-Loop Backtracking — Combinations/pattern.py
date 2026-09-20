def dfs(start, comb):

    if len(comb)==k:
        # do something

    for i in range(start, len(nums)):

        comb.append(nums[i])

        dfs(i + 1, )

        comb.pop()