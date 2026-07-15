from typing import List
import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        
        max_heap= []

        for num in nums:

            if num % 2 == 0:
                num= -num   
            else:
                num *=2

            heapq.heappush(max_heap,num)

        min_deviation= float('inf')
        min_val= - max(max_heap)

        