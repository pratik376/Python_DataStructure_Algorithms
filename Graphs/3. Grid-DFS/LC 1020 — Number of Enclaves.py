from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        ROWS, COLS= len(grid), len(grid[0])
        directions= [(1,0),(-1,0),(0,1),(0,-1)]

        visited= set()
        answer=0

        def dfs(i,j):

            stack=[(i,j)]
            visited.add((i,j))
            isBoundry=0

            if grid[i][j]==1 and (i==0 or i==ROWS-1) or (j==0 or j==COLS-1):
                isBoundry=1

            elif grid[i][j]==1 and ( 0<i and i>ROWS)  and ( 0<j and j < ROWS):
                answer+=1

            for r,c in directions:

                nR,nC= r+i, c+j

                if nR < 0 or nC< 0 or nR==ROWS or nC==COLS or (nR,nC) in visited or grid[nR][nC]==0:
                    continue
                


            

            







        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j]==1 and not (i,j) in visited:
                    dfs(i,j)
        