class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:

        res=[]
        subset=[]

        def dfs(i,xor):

            if i>=len(nums):
                return xor

            # add
            # what i was about to do xor+= xor ^ nums[i]
            include=dfs(i+1, nums[i] ^ xor)
            # remove  xor-= xor ^ nums[i]
            exclude=dfs(i+1, xor)

            return include + exclude

        return dfs(0,0)

        