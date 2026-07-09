from typing import List
import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        

       gifts=[ -val for val in gifts] # 0(N)

       heapq.heapify(gifts)  # O(N)

       while k >0:
          largets= -heapq.heappop(gifts) # O(log(n))

          cal_val=-math.floor(math.sqrt(largets)) 

          heapq.heappush(gifts,cal_val ) # logn
          k-=1
     

       return -sum(gifts)

        

           







        