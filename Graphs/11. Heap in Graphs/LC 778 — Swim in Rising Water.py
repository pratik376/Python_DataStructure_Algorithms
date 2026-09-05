from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        ROWS, COLS= len(grid),len(grid[1])

        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        visited=set()



        heap= [(grid[0][0],0,0)] # (time, i,j)


        while heap:

            t, i, j =heapq.heappop(heap)

            if (i,j) == (ROWS-1, COLS-1):
                return t

            if (i,j) in visited:
                continue

            visited.add((i,j))

        
            for nr,nc in directions:

                nr,nc= nr+i, nc+j

                if nr < 0 or nc< 0 or nr>=ROWS or nc>=COLS or (nr,nc) in visited:
                    continue
                max_time= max(t, grid[nr][nc])

                heapq.heappush(heap, (max_time, nr,nc))

        

            
        


