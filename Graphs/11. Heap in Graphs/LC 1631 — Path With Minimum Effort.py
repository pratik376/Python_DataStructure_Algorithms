from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        ROWS, COLS= len(heights), len(heights[0])

        directions= [(1,0),(-1,0),(0,1),(0,-1)]

        visited=set()
        answer=0

        minHeap= [(heights[0][0], 0, 0)]

        while minHeap:

            element, r,c = heapq.heappop(minHeap)

            if (r,c) in visited:
                continue

            visited.add((r,c))
            answer = max(answer,element)

            if r==ROWS-1 and c==COLS-1:
                return answer

            for nr,nc in directions:

                Nr,Nc= r+nr, c+nc

                if Nr < 0 or Nc < 0 or Nr>=ROWS or Nc>=COLS:
                    continue

                if (Nr,Nc) not in visited:

                    heapq.heappush(minHeap, (abs(element- heights[Nr][Nr]),Nr,Nc))

            



        