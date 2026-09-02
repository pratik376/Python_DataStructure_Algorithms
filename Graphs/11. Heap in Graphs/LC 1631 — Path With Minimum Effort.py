from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        ROWS, COLS= len(heights), len(heights[0])

        directions= [(1,0),(-1,0),(0,1),(0,-1)]

        visited=set()  # space (M+N)

        minHeap= [(0, 0, 0)] #   (M+N) * log(M+N)

        while minHeap:

            diff, r,c = heapq.heappop(minHeap)

            if (r,c) in visited:
                continue

            visited.add((r,c))
       

            if r==ROWS-1 and c==COLS-1:
                return diff

            for nr,nc in directions:

                Nr,Nc= r+nr, c+nc

                if Nr < 0 or Nc < 0 or Nr>=ROWS or Nc>=COLS or (Nr,Nc) in visited:
                    continue

                if (Nr,Nc) not in visited:

                    new_diff=max(diff, abs(heights[r][c]- heights[Nr][Nc]))

                    heapq.heappush(minHeap, (new_diff,Nr,Nc))

            



        