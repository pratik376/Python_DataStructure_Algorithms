from typing import List
import heapq

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        heap=[]

        for w in range(len(workers)):

            wx,wy= workers[w]

            for b in range(len(bikes)):
                bx,by= bikes[b]

                dist= abs(wx-bx) + abs(wy-by)
                heapq.heappush(heap, (dist,w,b))
            

            res=[-1] * len(workers)

            worker_used=[False] * len(workers)
            bike_used=[False]* len(bikes)

            while heap:

                dist, w, b= heapq.heappop(heap)

                if not worker_used[w] and not bike_used[b]:
                    worker_used[w]=True
                    res[w]=b
                    bike_used[b]=True
            return res