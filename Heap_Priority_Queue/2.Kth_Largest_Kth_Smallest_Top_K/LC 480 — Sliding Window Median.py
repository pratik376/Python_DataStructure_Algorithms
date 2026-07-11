from typing import List
import heapq
# two heap time
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
       heap=[]
       answer=[]

       for i in range(len(nums)):
           
           
           heapq.heappush(heap,(nums[i],i))
           while (heap[0][1] + (k-1) ) < i:
                   heapq.heappop(heap)
           if i >= k-1:
               
               answer.append(heap[0][0])
        
       return answer