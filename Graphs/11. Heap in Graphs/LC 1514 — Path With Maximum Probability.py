from typing import List

from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:


        adj= defaultdict(list)

        for a,b , prob in zip(edges,succProb):
            adj[a].append((b,prob))
            adj[b].append((a,prob))

        max_heap=[(-1,start_node)]

        visited=set()


        while max_heap:

            w1, node =heapq.heappop(max_heap)
            w1=-w1
    
            if node in visited:
                continue
    
            if node == end_node:
                return w1
        
            visited.add(node)

            for n2, prob in adj[node]:

                if n2 not in visited:
                    heapq.heappush(max_heap,(-(w1* prob),n2))

        return 0

        

        