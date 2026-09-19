class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:


        res=[]
        subset=[]

        def dfs(i):

            if i>= len(nums):
                res.append(subset.copy())
                return


            # keep
            subset.append(nums[i])
            dfs(i+1)

            # remove
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res