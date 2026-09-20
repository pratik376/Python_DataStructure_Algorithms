from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

       
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
            


        