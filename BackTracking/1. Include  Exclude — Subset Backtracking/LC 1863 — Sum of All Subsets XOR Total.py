class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:

        res=[]
        subset=[]

        def dfs(i,xor):

            if i ==len(nums)-1:
                return xor

            # add
            # what i was about to do xor+= xor ^ nums[i]
            dfs(i+1, nums[i] ^ xor)
            # remove  xor-= xor ^ nums[i]
            dfs(i+1, xor)

        return dfs(0,0)

        