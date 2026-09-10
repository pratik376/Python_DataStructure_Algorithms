
from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]],start: List[int],destination: List[int]) -> bool:



        ROWS, COLS= len(maze), len(maze[0])
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

                while (0<= nr+R <ROWS and 0<= nc+C <COLS and maze[nr+R][nc+C]==1):
                    nr+=R
                    nc+=C

                if ((nr,nc)) not in visited and 0<= nr+R <ROWS and 0<= nc+C <COLS:
                    visited.add((nr,nc))
                    stack.append((nr,nc))

        return False
            

    




        