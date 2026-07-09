from typing import List
import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        

       gifts=[ -val for val in gifts]

       heapq.heapify(gifts)

       while k >0:
          largets= -heapq.heappop(gifts)

          cal_val=-math.floor(math.sqrt(largets))

          heapq.heappush(gifts,cal_val )
          k-=1
       gifts=[ -val for val in gifts]

       return sum(gifts)

        

           







        