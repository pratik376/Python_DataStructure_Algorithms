from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid),len(grid[0])
        visited=set()

        directions= [(1,0),(-1,0),(0,1),(0,-1)]

        answer=0


        def dfs(i,j):

            stack=[(i,j)]
            island=0
            visited.add((i,j))

            while stack:

                i, j = stack.pop()
                island+=1
                for r, c in directions:

                    nR,nC = r + i, c + j

                    if nR < 0 or nC< 0 or nR==ROWS or nC==COLS or (nR,nC) in visited or grid[nR][nC]==0:
                        continue

                    visited.add((nR,nC))
                    stack.append((nR,nC))

            return island


        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j]==1 and (i,j) not in visited:

                    answer= max(answer, dfs(i,j))

        return answer
