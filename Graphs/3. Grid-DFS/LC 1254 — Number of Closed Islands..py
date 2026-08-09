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
                




        for i in range(ROWS):
            for j in range(COLUMNS):

                if grid[i][j]==0 and (i,j) not in visited:

                    if dfs(i,j):
                        closed_island+=1



















