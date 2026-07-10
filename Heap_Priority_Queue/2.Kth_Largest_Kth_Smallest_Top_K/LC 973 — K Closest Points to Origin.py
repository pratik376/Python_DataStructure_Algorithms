

from typing import List
import heapq
import math
# first i code then i watch video

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        mini_heap=[]

        for point in points:

            x,y= point

            sq_distance= math.sqrt( x ** 2 + y **2)

            heapq.heappush(mini_heap, (sq_distance,point))

            if len(mini_heap) > k:
                heapq.heappop(mini_heap)
        return mini_heap[0][1]



        