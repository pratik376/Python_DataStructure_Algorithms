from typing import List
import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        heap= [ -val for val in nums]

        heapq.heapify(heap)

        score=0

        for _ in range(k):

            element= -heapq.heappop(heap)

            score+= element

            heapq.heappush(heap, - (math.ceil(element/3)))
        
        return score






        