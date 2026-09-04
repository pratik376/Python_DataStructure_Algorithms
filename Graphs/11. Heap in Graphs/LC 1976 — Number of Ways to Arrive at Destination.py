from typing import List
import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        adj=defaultdict(list)
        MOD= 10 **9 +7


        for a, b, cost in roads:

            adj[a].append((b,cost))
            adj[b].append((a,cost))


        min_cost= [float("inf")] * n
        min_cost[0]=0
        path_count=[0] * n
        path_count[0]=1

        heap= [(0,0)] # cost, node

ssda
        while heap:

            cost, node =heapq.heappop(heap)

            for nei, nei_cost in adj[node]:

                new_cost= cost + nei_cost

                if new_cost < min_cost[nei]:
                    min_cost[nei]=new_cost
                    path_count[nei]=path_count[node]

                elif new_cost== min_cost[nei]:
                    path_count[nei]= (path_count[nei]+path_count[node]) % MOD

        return min_cost[n-1]
        