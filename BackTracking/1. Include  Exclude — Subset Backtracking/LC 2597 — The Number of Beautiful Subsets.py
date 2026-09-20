from typing import List
from collections import defaultdict

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        count =0
        subset=[]

        def dfs(i,subset):
            nonlocal count

            if i>= len(nums):
                return

            # keep

            can_include=True
            for element in subset:

                if abs(element - nums[i])==k:
                    can_include=False
                    break

            if can_include:
                count+=1
                subset.append(nums[i])
                dfs(i+1, subset)
                subset.pop()
            dfs(i+1,subset)

        dfs(0,subset)

        return count

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        count =0
        freq=defaultdict(int)

        def dfs(i):
            nonlocal freq,count

            if i>= len(nums):
                return


            x=nums[i]

            if freq[x-k]==0 and freq[x+k]==0:
                count+=1

                freq[x]+=1
                dfs(i+1)
                freq[x]-=1

            dfs(i+1)

        dfs(0)

        return count

            


        