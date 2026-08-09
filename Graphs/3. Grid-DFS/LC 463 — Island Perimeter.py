from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        ROWS, COLUMS =len(grid), len(grid[0])
        visited= set()
        answer=0

        directions= [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(i,j):

            stack=[(i,j)]


            while stack:
                i,j =stack.pop()

                if (i,j) not in visited and i>= len(grid) or j>=len(grid[0]) or i<0 or j< 0 or grid[i][j]==0:
                    answer+=1

                visited.add((i,j))


                for R,C in directions:
                    nR,nC= R+i,C+j

                    if (nR,nC) in visited :
                        continue

                    if nR>= len(grid) or nC>=len(grid[0]) or nR<0 or nC< 0 or grid[nR][nC]==0:
                        answer+=1

                    if not grid[nR][nC] ==0:

                        visited.add((nR,nC))
                        stack.append((nR,nC))


        for i in range(ROWS):
            for j in range(COLUMS):

                if grid[i][j] != 0 and (i,j) not in visited:

                    dfs(i,j)
        return answer