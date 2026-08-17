from typing import List
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:


        if not grid:
            return -1

        
        visited= set()
        ROWS,COLS= len(grid), len(grid[0])
        directions= [(1,0),(-1,0),(0,1),(0,-1)]

        q=deque()

        answer=-1

        zeros=[]
        ones=[]



        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j]==1:
                    q.append((i,j,0))
                    visited.add((i,j))

                if grid[i][j]==0:
                    zeros.append(0)
                if grid[i][j]==1:
                    ones.append(1)

        if len(zeros) == ROWS * COLS or len(ones) == ROWS * COLS:
            return -1

    

        while q:
            i,j,dist =q.popleft()

            answer=max(answer,dist)

            for r,c in directions:

                nR,nC= r+i, c+j

                if nR < 0 or nC <0 or nR>=ROWS or nC>=COLS or (nR,nC) in visited:
                    continue

                visited.add((nR,nC))
                q.append((nR,nC,dist+1))



        return answer





        