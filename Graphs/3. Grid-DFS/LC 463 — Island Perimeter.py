from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        ROWS, COLUMS =len(grid), len(grid[0])
        visited= set()
        answer=0

        directions= [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(i,j):

            stack=[i,j]


            while stack:
                i,j =stack.pop()

                for R,C in directions:
                    nR,nC= R+i,C+j

                    if nR <0 or nC < 0 or nR>=ROWS or nC>=COLUMS or (nR,nC) in visited or grid[nR][nC]==0:
                        continue

                    if nR==-1 or nR==ROWS+1 or nC== -1 or nC== COLUMS+1 or grid[nR][nC]==0:
                        answer+=1

                    visited.add((nR,nC))
                    stack.append((nR,nC))


        for i in range(ROWS):
            for j in range(COLUMS):

                if grid[i][j] != 0 and (i,j) not in visited:

                    dfs(i,j)
        return answer