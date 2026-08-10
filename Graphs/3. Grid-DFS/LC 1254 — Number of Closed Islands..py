from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid),len(grid[0])
        visited= set()
        closed_island=0

        directions = [(0,1),(0,-1),(-1,0),(1,0)]

        def dfs(i,j):

            stack=[(i,j)]
            visited.add((i,j))


            while stack:
                i,j = stack.pop()
                isIsland=True


                for r,c in directions:

                    nR,nC= r+i, c+j

                    if nR < 0 or nR >=ROWS or nC< 0 or nC >= COLUMNS or  (nR,nC) in visited or grid[nR][nC]==1:
                        continue

                    if grid[nR][nC]== 0 and (nR==0 or nR==ROWS-1 or nC==0 or nC== COLUMNS-1):
                        visited.add((nR,nC))
                        isIsland=False

                    visited.add((nR,nC))
                    stack.append((nR,nC))

            return isIsland



        for i in range(ROWS):
            for j in range(COLUMNS):

                if grid[i][j]==0 and (i,j) not in visited:

                    if dfs(i,j):
                        closed_island+=1

        return closed_island



















