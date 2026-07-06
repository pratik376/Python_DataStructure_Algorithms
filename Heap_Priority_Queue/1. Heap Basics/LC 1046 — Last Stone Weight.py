from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) < 2:
            return stones[0]
        
        heap=[]

     
        
        for i in range(len(stones)):

            heapq.heapify_max(heap, stones[i])
        
        while len(heap)>=2:
            x= heapq.heappop_max(heap)
            y= heapq.heappop_max(heap)

            if x != y:
                heapq.heappush_max(x-y)
        
        return heap[0] if len(heap) else 0
        

        
        



        

        