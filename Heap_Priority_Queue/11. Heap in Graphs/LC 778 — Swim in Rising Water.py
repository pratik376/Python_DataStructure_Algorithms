from typing import List
import heapq
from collections import defaultdict


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        ROWS,Columns= len(grid[0]), len(grid[1])

        visited= set()

        minHeap = [[grid[0][0], 0, 0]]  # current_max,row ,column
        directions= [[0,1], [0,-1], [1,0],[-1,0]]
        
        