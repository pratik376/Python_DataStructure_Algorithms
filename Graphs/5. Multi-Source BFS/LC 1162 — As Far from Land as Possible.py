from typing import List
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:



        visited= set()
        ROWS,COLS= len(grid), len(grid[0])
        directions= [(1,0),(-1,0),(0,1),(0,-1)]




        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j]==





        