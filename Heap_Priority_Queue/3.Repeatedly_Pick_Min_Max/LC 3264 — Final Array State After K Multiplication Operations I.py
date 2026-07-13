from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        heapq.heapify(nums)

        for _ in range(k):

            element=heapq.heappop(nums)

            heapq.heappush(nums, multiplier * element)
        
        return nums


        