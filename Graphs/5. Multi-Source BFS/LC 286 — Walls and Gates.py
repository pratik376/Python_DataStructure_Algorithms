from typing import List
from collections import deque
class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:


        visited=set()
        ROWS,COLS= len(grid), len(grid[0])
        directions= [(1,0),(-1,0),(0,1),(0,-1)]

        q=deque()

        INF= 2147483647
        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j]==0:
                    q.append((i,j,0))
                    visited.add((i,j))

        while q:
            i,j, dist= q.popleft()

            for r,c in directions:
                nR,nC= r+i, c+j

                if nR < 0 or nC <0 or nR>=ROWS or nC>=COLS or (nR,nC) in visited or grid[nR][nC]==-1:
                    continue
                grid[nR][nC]= dist+1

                q.append((nR,nC,dist+1))
                visited.add((nR,nC))


        


      


                
                