from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS1, COLS1 = len(grid1), len(grid1[0])
        ROWS2, COLS2 = len(grid2), len(grid2[0])
        
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        