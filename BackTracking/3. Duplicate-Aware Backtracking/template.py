nums.sort()

def dfs(start):
    for i in range(start, len(nums)):

        if i > start and nums[i] == nums[i - 1]:
            continue

        path.append(nums[i])
        dfs(i + 1)
        path.pop()