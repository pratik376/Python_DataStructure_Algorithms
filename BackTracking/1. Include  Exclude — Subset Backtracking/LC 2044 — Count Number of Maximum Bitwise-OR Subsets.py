class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:

        max_OR = 0

        for num in nums:

            max_OR |= num

        count = 0

        def dfs(i, Nor):
            nonlocal count

            if i == len(nums):
                if Nor == max_OR:
                    count += 1
              
            # add

            dfs(i + 1, Nor | nums[i])

            # not add

            dfs(i + 1, Nor)

        return count
