from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visited= set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i,j):

            stack= [(i,j)]
            visited.add((i,j))
            isClosed= True
            

            while stack:

                i, j = stack.pop()

                if i==0 or j == 0 or i == ROWS-1 or j== COLS-1:
                    isClosed=False

                for r,c in directions:

                    nR,nC = r+i, c+j

                    if nR < 0 or nC< 0 or nR==ROWS or nC==COLS or (nR,nC) in visited or grid[nR][nC]==1:
                        continue
                    visited.add((nR,nC))
                    stack.append((nR,nC))

            return isClosed           

                
        answer =0
        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j]==0 and (i,j) not in visited:

                    if dfs(i,j):
                        answer+=1
        return answer
        