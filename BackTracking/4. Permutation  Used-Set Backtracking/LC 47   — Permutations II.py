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

                if used[i]:
                    continue

                used[i]=True
                path.append(nums[i])

                dfs(path)

                path.pop()

               
                while i+1 < len(nums) and nums[i] == nums[i+1]:
                    used[i]=True
                    i+=1
                
        dfs([])
        return res
                