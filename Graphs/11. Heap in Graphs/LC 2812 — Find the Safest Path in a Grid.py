from typing import List
from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
        N=len(grid)

        def in_bound(r,c):
            return min(r,c)>=0 and max(r,c)<N

        def precompute():
            q=deque()
            min_dist={}

            for r in range(N):
                for c in range(N):

                    if grid[r][c]:
                        q.append((r,c,0))
                        min_dist[(r,c)]=0

            while q:
                r,c, dist=q.popleft()

                neighbour= [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]

                for r2,c2 in neighbour:

                    if in_bound(r2,c2) and (r2,c2) not in min_dist:
                        min_dist[(r2,c2)]= dist+1
                        q.append((r2,c2, dist+1))
            return min_dist

        min_dist=precompute()
        maxHeap= [(-min_dist[(0,0)], 0,0)] # (dist,r,c)
        visited= set()

        while maxHeap:
            dist, r,c = heapq.heappop(maxHeap)
            dist=-dist

            if (r,c)==(N-1,N-1):
                return dist

            if (r,c) in visited:
                continue
            visited.add((r,c))

            neighbour= [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            for r2,c2 in neighbour:

                if  in_bound(r2,c2) and (r2,c2) not in visited:
                    dist2= min(dist, min_dist[(r2,c2)])
                    heapq.heappush(maxHeap, (-dist2, r2,c2))




    