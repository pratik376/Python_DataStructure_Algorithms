

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

            heapq.heappush(mini_heap, (-sq_distance,point))

            if len(mini_heap) > k:
                heapq.heappop(mini_heap)
        return [point for distance, point in mini_heap]

from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (-dist, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)

        return [point for _, point in heap]


        