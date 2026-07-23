from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        heap=[] # max_heap


        for i in range(len(heights)-1):

            diff= heights[i+1] - heights[i]

            if diff <=0:
                continue

            bricks-=diff
            heapq.heappush()






