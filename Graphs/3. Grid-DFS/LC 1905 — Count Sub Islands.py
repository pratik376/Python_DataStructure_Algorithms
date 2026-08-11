from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
       
        ROWS2, COLS2 = len(grid2), len(grid2[0])
        
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]


        def dfs(i,j):

            stack=[(i,j)]
            visited.add((i,j))
            isSubIsland=True

            while stack:

                i,j=stack.pop()

                if not grid1[i][j]:
                    isSubIsland=False


                for r,c in directions:

                    nR, nC= r+i, c+j

                    if nR < 0 or nC< 0 or nR==ROWS2 or nC==COLS2 or (nR,nC) in visited or grid2[nR][nC]==0:
                        continue

                    visited.add((i,j))
                    stack.append((i,j))

            return isSubIsland


        sub_island=0
        for i in range(ROWS2):
            for j in range(COLS2):

                if grid2[i][j]== 1 and (i,j) not in visited:

                    if dfs(i,j):
                        sub_island +=1

        return sub_island
        