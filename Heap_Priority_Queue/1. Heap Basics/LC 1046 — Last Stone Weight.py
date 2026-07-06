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
        
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
       
        stones=[-val for val in stones]

        heapq.heapify(stones) # it takes one list na donly one argument
        
        while len(stones)>=2:
            x= -heapq.heappop(stones)
            y= -heapq.heappop(stones)

            if x != y:
                heapq.heappush_max(stones,-(x-y))
        
        return -stones[0] if stones else 0
        

        
        



        

        