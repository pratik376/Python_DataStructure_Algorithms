from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS,COLS= len(grid), len(grid[0])
        directions= [(1,0),(-1,0),(0,1),(0,-1)]

        visited= set()
        answer=0

        def BFS(q):
            nonlocal answer

            while q:

                i,j,time= q.popleft()

                answer=max(answer,time)


                for r,c in directions:

                    nR,nC= r+i, j+c

                    if nR < 0 or nC <0 or nR>=ROWS or nC>=COLS or (nR,nC) in visited or grid[nR][nC]==0:
                        continue

                    q.append((nR,nC,time+1))
                    visited.add((nR,nC))

        q=deque()
        
        non_zero_count=0
        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j]!=0:
                    non_zero_count+=1

                if grid[i][j]==2:
                    visited.add((i,j))
                    q.append((i,j,0))

        BFS(q)  

        return answer if non_zero_count == len(visited) else -1
        