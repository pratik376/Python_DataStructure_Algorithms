from typing import List
import heapq
from collections import defaultdict

class Solution:
    def maximumMinimumValuePath(self, heights: List[List[int]]) -> int:

        ROWS, COLUMS= len(heights), len(heights[0])

        maxHeap = [[-heights[0][0],0,0]] # (diff, r,c)
        visited= set()
        
        directions= [[0,1], [0,-1], [1,0],[-1,0]]

        while maxHeap:

            diff, r,c = heapq.heappop(maxHeap)
            diff = -diff

            if (r,c) in visited:

                continue

            visited.add((r,c))

            if (r,c)==(ROWS-1, COLUMS-1):
                return diff

            for dr,dc in directions:
                newR,newC= r+ dr , c+dc

                if newR < 0 or newC < 0 or newR==ROWS or newC==COLUMS or (newR,newC) in visited:
                    continue 

                newDiff= min(diff, heights[newR][newC])
                heapq.heappush(maxHeap, [-newDiff, newR,newC])


