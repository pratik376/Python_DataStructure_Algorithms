import heapq
from typing import List
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        min_hep, max_heap= [], []
        answer=[]
        delayed= defaultdict(int)

        target = 'odd' if k%2!=0 else 'even'

        for i in range(len(nums)):

            if not max_heap or nums[i]<= - max_heap[0]: 
                heapq.heappush(max_heap, - nums[i])
            
            else:
                heapq.heappush(min_hep, nums[i])
            
            if len(max_heap) > len(min_hep) +1 :
                heapq.heappush(min_hep, -heapq.heappop(max_heap))
            elif len(min_hep) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_hep))
            
            if i >= k-1:

                if target=='odd':
                    answer.append(-max_heap[0])
                
                else:
                    answer.append((-max_heap[0] + min_hep[0]) / 2)
        return answer





            
      
