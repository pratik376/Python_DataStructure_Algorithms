from typing import List
import heapq

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
       
       ROWS, COLS= len(grid),len(grid[0])
       directions=[(1,0),(-1,0),(0,1),(0,-1)]
       visited=set()

       heap=[(grid[0][0], 0,0)]


       while heap:

           condition, r,c =heapq.heappop(heap)

           if (r,c) in visited:
               continue

           visited.add((r,c))

           if (r,c) == (ROWS-1, COLS-1):
               return condition


           for R,C in directions:
               R,C= R+r, C+c

               if R<0 or C<0 or R>=ROWS or C>=COLS or (R,C) in visited:
                   continue

               heapq.heappush(heap,(condition+ grid[R][C], R,C)) 
    


       
        