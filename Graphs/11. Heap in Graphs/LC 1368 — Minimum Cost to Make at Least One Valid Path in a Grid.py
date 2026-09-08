from typing import List
import heapq

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        ROWS, COLS= len(grid),len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        visited=set()


        heap=[(0,(0,0))] # cost, cordinates 
    


        while heapq:

            cost, i, j=heapq.heappop(heap)

            if (i,j) in visited:
                continue

            if (i,j)==(ROWS-1,COLS-1):
                return cost

            visited.add((i,j))

            for r,c in directions:

                nr,nc=r+i,c+j

                if nr < 0 or nc <0 or nc >=COLS or nr >=ROWS or (nr,nc) in visited:
                    continue

                if ((r,c)==(1,0) and grid[nr][nc]==3) or ((r,c)==(0,1) and grid[nr][nc]==1) or ((r,c)==(-1,0) and grid[nr][nc]==4) or ((r,c)==(0,-1) and grid[nr][nc]==2):
                    heapq.heappush(heap,(cost,(nr,nc)))
                else:
                    heapq.heappush(heap, (cost+1, (nr,nc)))
                    
                



        