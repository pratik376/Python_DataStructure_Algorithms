from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:


        ROWS, COLUMS= len(grid), len(grid[0])
        directions= [(1,0),(-1,0),(0,1),(0,-1)]
        visited= set()

        answer=0

        def dfs(i,j):

            fish=0

            stack=[(i,j)]

            if (i,j) not in visited and grid[i][j]>=1:
                fish+=grid[i][j]

            visited.add((i,j))

            while stack:

                for R,C in directions:

                    nR,nC = R+i, C+j

                    if nR < 0 or nC< 0 or nR>=ROWS or nC>=COLUMS or (nR,nC) in visited or grid[nR][nC] ==0:
                        continue

                    visited.add((nR,nC))
                    stack.append((nR,nC))
                    fish+=grid[nR][nC]

            return fish
        

        for i in range(ROWS):
            for j in range(COLUMS):

                if grid[i][j]>=1 and (i,j) not in visited:

                    answer= max(answer,dfs(i,j))

        return answer