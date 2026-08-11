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
            island=0

            while stack:

                i, j = stack.pop()

                for r,c in directions:

                    nR,nC = r+i, c+j

                    if nR < 0 or nC< 0 or nR==ROWS or nC==COLS or (nR,nC) in visited:
                        continue

                    if grid[nR][nC]== 0 and nR==0 or nC==0 or nR==ROWS-1 or nC==COLS -1:
                        isClosed=False
                        visited.add((i,j))
                        stack.append((i,j))

                    if grid[nR][nC]==1 and nR in [0, ROWS-1] and nC in [0,COLS-1]:
                        island+=1

            return island if isClosed else 0            

                
        answer =0
        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j]==0 and (i,j) not in visited:

                    if dfs(i,j):
                        answer+=1
        return answer
        