from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visited= set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i,j):










        answer =0
        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j]==0 or (i,j) not in visited:

                    answer += dfs(i,j)
        return answer
        