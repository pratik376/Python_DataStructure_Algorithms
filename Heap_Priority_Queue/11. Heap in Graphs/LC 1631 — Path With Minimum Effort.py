from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        ROWS, COLUMS= len(heights), len(heights[0])

        minHeap = [[0,0,0]] # (diff, r,c)
        visit= set()
        
        directions= [[0,1], [0,-1], [1,0],[-1,0]]

        while minHeap:

            diff, r,c = heapq.heappop(minHeap)
            

