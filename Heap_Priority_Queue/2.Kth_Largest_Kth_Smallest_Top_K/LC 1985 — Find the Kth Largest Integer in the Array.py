from typing import List
import heapq
from collections import defaultdict

class solution:
    def KthLargestInt(self, nums: List[int], k:int) -> int:

        mini_heap=[]

        for val in nums:
            heapq.heappush(mini_heap,val)  # (log K)

            if len(mini_heap)>k:
                heapq.heappop(mini_heap) # (log (K))
        
        return mini_heap[0] 

class Solution:
    def kthLargestNumber(self, nums: List[str], k:int) -> str:

        mini_heap=[]

        for val in nums:
            val= int(val)
            heapq.heappush(mini_heap,val)  # (log K)

            if len(mini_heap)>k:
                heapq.heappop(mini_heap) # (log (K))
        
        return str(mini_heap[0]) 