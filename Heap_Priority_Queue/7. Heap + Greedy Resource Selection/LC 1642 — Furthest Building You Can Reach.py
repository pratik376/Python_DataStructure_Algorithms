from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        heap=[] # max_heap


        for i in range(len(heights)-1):

            diff= heights[i+1] - heights[i]
            





