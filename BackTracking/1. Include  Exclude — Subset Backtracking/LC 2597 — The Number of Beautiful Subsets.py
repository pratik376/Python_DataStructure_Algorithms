from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        count =0
        subset=[]

        def dfs(i,subset):
            nonlocal count

            if i>= len(nums):
                return

            # keep

            flag=0
            for element in subset:

                if abs(element - nums[i])!=k:
                    flag=1

            if not flag:
                count+=1

            subset.append(nums[i])
            dfs(i+1, subset)

            # remove
            subset.pop()
            dfs(i+1,subset)

        dfs(0,subset)

        return count

            


        