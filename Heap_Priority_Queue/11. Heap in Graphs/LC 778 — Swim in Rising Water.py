from typing import List
import heapq
from collections import defaultdict


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        ROWS,Columns= len(grid), len(grid[0])

        visited= set()

        minHeap = [[grid[0][0], 0, 0]]  # current_max,row ,column
        directions= [[0,1], [0,-1], [1,0],[-1,0]]

        while minHeap:

            curr_val, r, c = heapq.heappop(minHeap)

            if  (r,c) in visited:
                continue

            visited.add((r,c))

            if r== ROWS-1 and c== Columns-1:
                return curr_val

            for dr,dc in directions:
                newR,newC= r+ dr , c+dc
            
                if newR < 0 or newC < 0 or newR==ROWS or newC==Columns or (newR,newC) in visited:
                    continue 

                new_diff= max(curr_val, grid[newR][newC])

                heapq.heappush(minHeap, (new_diff, newR,newC))
