def dfs(i):

    if i == len(nums):
        return valid_solution()

    for bucket in range(k):

        if can_place(nums[i], bucket):

            buckets[bucket] += nums[i]

            if dfs(i + 1):
                return True

            buckets[bucket] -= nums[i]

    return False