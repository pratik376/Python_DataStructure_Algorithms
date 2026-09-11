
from typing import List
from collections import deque
import heapq
class Solution:
    def hasPath(self, maze: List[List[int]],start: List[int],destination: List[int]) -> bool:



        ROWS, COLS= len(maze), len(maze[0])
        visited=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        q=[]
        q.append((0, start[0],start[1]))
        


        while q:

            cost,r,c=heapq.heappop(q)
            if (r,c)==tuple(destination):
                return cost

            if (r,c) in visited:
                continue

            visited.add((r,c))

            for R,C in directions:

                nr,nc= r,c
                steps=0

                while (0<= nr+R <ROWS and 0<= nc+C <COLS and maze[nr+R][nc+C]==0):
                    nr+=R
                    nc+=C
                    steps+=1

                if ((nr,nc)) not in visited:
                    heapq.heappush(q, (cost+steps, nr,nc ))

        return -1
            

    




        