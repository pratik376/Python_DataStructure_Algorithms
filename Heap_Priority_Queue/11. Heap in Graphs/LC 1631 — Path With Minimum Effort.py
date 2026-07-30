from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        ROWS, COLUMS= len(heights), len(heights[0])

        minHeap = [[0,0,0]] # (diff, r,c)
        visited= set()
        
        directions= [[0,1], [0,-1], [1,0],[-1,0]]

        while minHeap:

            diff, r,c = heapq.heappop(minHeap)

            if (r,c) in visited:

                continue

            visited.add((r,c))

            if (r,c)==(ROWS-1, COLUMS-1):
                return diff

            for dr,dc in directions:
                newR,newC= r+ dr , c+dc

                if newR < 0 or newC < 0 or newR==ROWS or newC==COLUMS or (newR,newC) in visited:
                    continue 

                newDiff= max(diff, abs(heights[r][c]-heights[newR][newC]))
                heapq.heappush(minHeap, [newDiff, newR,newC])


