
from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]],start: List[int],destination: List[int]) -> bool:




        visited=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        stack=[start]
        visited.add(start)


        while stack:

            r,c=stack.pop()

            if (r,c)==destination:
                return True

            for R,C in directions:

                nr,nc= r,c
                



        