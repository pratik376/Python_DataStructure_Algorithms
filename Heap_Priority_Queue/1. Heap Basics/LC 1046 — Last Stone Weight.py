from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) < 2:
            return stones[0]
        
        
        