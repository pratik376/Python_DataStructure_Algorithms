from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        k= len(nums)

        left=right= nums[0][0]

        for i in range(k):
            
