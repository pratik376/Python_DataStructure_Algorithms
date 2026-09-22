class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        
        res=[]
        used=[False] * len(nums)

        def dfs(path):

            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):

                if i> 0 and nums[i]== nums[i-1] and not used[i-1]:
                    continue

                if used[i]:
                    continue

                used[i]=True
                path.append(nums[i])

                dfs(path)

                path.pop()
                used[i]=False   
        dfs([])
        return res
                