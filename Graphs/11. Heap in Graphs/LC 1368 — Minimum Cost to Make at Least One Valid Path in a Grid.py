from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        ROWS, COLS= len(grid),len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        visited=set()


        