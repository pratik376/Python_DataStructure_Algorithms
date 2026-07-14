from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        heap = [(val,index) for index, val in enumerate(nums) ]

        heapq.heapify(heap)

        for _ in range(k):

            val, index = heapq.heappop(heap)

            heapq.heappush(heap, (val * multiplier))

            nums[index]=val * multiplier
        return nums



       
    

        