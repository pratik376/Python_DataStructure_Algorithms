from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands=0

        ROWS, COLUMS= len(grid), len(grid[0])

        visited= set()
        directions= [ [1,0],[-1,0],[0,1],[0,-1]]

        

        def dfs(i,j):
            stack=[(i,j)]
            visited.add((i,j))

            while stack:

                i, j = stack.pop()


                for R,C in directions:
                    nR,nC= R+i, C+j

                    if nR < 0 or nC < 0 or (nR,nC) in visited:
                        continue
                    visited.add((nR,nC))
                    stack.append((nR,nC))

                


        for i in range(ROWS):
            for j in range(COLUMS):

                if grid[i][j]=='1' and (i,j) not in visited:
                    islands+=1
                    dfs(i,j)


        