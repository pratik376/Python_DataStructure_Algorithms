class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:

        res=[]
        subset=[]

        def dfs(i,xor):

            if i >len(nums):
                return xor


            # add
            
        
            dfs(i+1, nums[i] * xor)

            # remove
            dfs(i+1, xor)

        return dfs(0,0)

        