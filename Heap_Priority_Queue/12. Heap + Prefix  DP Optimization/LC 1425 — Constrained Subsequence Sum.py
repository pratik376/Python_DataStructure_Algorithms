from typing import List
import heapq


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        res=nums[0]

        heap_max=[(nums[0],0)] # max_sum, index
        
        
        