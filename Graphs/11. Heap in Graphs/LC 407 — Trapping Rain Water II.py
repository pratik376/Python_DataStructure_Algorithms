from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROWS, COLS = len(heightMap), len(heightMap[0])

        Heap=[]

        for r in range(ROWS):
            for c in range(COLS):

                if r in [0, ROWS-1] or c in [0,COLS-1]:
                    heapq.heappush(Heap,(heightMap[r][c],r,c))
                    heightMap[r][c]=-1 # visited


        res=0
        max_h=-1

        while Heap:
            height, r, c=heapq.heappop(Heap)

            max_h=max(max_h,height)
            res+= max_h -height

            nei=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]

            for nr,nc in nei:

                if (nr < 0 or nc<0 or nr>=ROWS or nc>=COLS or heightMap[nr][nc]==-1):
                    continue
                heapq.heappush(Heap,(heightMap[nr][nc],nr,nc))
                heightMap[nr][nc]=-1 # visited



