from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) < 2:
            return stones[0]
        
        heap=stones[:]

        heapq.heapify_max(heap) # it takes one list na donly one argument
        
        while len(heap)>=2:
            x= heapq.heappop_max(heap)
            y= heapq.heappop_max(heap)

            if x != y:
                heapq.heappush_max(heap,x-y)
        
        return heap[0] if heap else 0
        

        
        



        

        