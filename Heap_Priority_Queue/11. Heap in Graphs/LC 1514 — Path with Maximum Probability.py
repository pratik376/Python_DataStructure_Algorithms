from typing import List
import heapq
from collections import defaultdict


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        edges=defaultdict(list)  # (prob, node)
        i=0

        for start, des in edges:
            edges[start].append((succProb[i],des))
            i+=1

        visited= set()
        maxHeap= [(1, start_node)] # (prob, node)


        while maxHeap:
            prob, node= heapq.heappop(maxHeap)

            

            if node in visited:
                continue

            visited.add(node)

            for prob2, node2 in edges[node]:

                if not node2 in visited:

                    heapq.heappush(maxHeap,(prob*prob2,node2)) 





        