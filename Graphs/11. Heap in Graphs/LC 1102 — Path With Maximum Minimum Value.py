from typing import List
import heapq

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:

    

        maxheap= [(-grid[0][0],0,0)]

        ROWS, COLS= len(grid), len(grid[0])
        visited=set()
        directions= [(1,0),(-1,0),(0,1),(0,-1)]

        while maxheap:

            val , r, c = heapq.heappop(maxheap)
            val=-val

            if r ==ROWS-1 and c==COLS-1:
                return val

            if (r,c) in visited:
                continue

            visited.add((r,c))

            for nr,nc in directions:

                R,C= nr+r, nc+c

                if R< 0 or R==ROWS or C<0 or C==COLS or (R,C) in visited:
                    continue
                
                
                heapq.heappush(maxheap, (-min(val, grid[R][C]), R,C))


        