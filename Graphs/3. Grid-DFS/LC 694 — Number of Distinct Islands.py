from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        directions= [(1,0),(-1,0),(0,1),(0,-1)]
        visited= set()
        shapes=set()



        def dfs(i,j):

            statR,startC=i,j

            stack=[(i,j)]
            visited.add((i,j))

            while stack:

                i,j = stack.pop()

                shapes.append((i-statR,j-startC))

                for r,c in directions:
                    nR,nC= r+ i, c +j
                    





        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j]== 1 and (i,j) not in visited:
                    dfs(i,j)

        return 







        