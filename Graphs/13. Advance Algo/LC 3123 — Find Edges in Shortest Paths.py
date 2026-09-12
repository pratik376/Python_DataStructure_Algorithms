from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:

        adj = defaultdict(list)

        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))


        def dijkstra(src):

            dist = [float("inf")] * n
            dist[src] = 0

            heap = [(0, src)]

            while heap:

                cost, node = heapq.heappop(heap)

                if cost > dist[node]:
                    continue

                for nei, w in adj[node]:

                    new_cost = cost + w

                    if new_cost < dist[nei]:

                        dist[nei] = new_cost
                        heapq.heappush(heap, (new_cost, nei))

            return dist


        dist_start = dijkstra(0)
        dist_end = dijkstra(n - 1)

        shortest = dist_start[n - 1]

        answer = []

        for a, b, w in edges:

            path1 = dist_start[a] + w + dist_end[b]
            path2 = dist_start[b] + w + dist_end[a]

            if path1 == shortest or path2 == shortest:
                answer.append(True)
            else:
                answer.append(False)

        return answer