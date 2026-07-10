from typing import List
import heapq
from collections import defaultdict, Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq=Counter(nums)
        mini_heap =[]


        for num,count in freq.items():

            heapq.heappush(mini_heap,(count,num))

            if len(mini_heap) > k:
                heapq.heappop(mini_heap)
        
        return [num for count, num in mini_heap]
            
        
        
        
        
        
