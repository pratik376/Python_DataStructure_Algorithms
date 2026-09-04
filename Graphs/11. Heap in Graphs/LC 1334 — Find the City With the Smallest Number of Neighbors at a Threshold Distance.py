from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        adj= defaultdict(list)

        for a,b, dist in edges:
            adj[a].append((b,dist))
            adj[b].append((a,dist))



        def dijkstra(src):

            visited= set()
            heap=[(0,src)]

            while heap:

                dist, node =heapq.heappop(heap)

                if node in visited:
                    continue

                visited.add(node)

                for nei, dist2 in adj[node]:

                    if nei not in visited:

                        if dist+ dist2 <=distanceThreshold:

                            heapq.heappush(heap, ((dist+dist2,nei)))

            return len(visited)-1


        res, min_count= -1, n

        for src in range(n):

            count= dijkstra(src)

            if count<=min_count:

                res, min_count = src, count

        return res


        