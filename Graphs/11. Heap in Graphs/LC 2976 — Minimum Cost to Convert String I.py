from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:


        adj=defaultdict(list)

        for a,b, cost in zip(original,changed,cost):
            adj[a].append((b,cost))


        
        total_cost=0

        for i in range(len(source)):

            heap=[(0,source[i])]# cost, current node
            heapq.heappush(heap) 
            current_cost=0
            visited= set()

            while heap:

                cost, node =heapq.heappop()

                if node==target[i]:
                    current_cost+=cost
                    total_cost += current_cost
                    break

                if node in visited:
                    continue

                visited.add(node)

                for nei,ne_cost in adj[node]:

                    if nei not in visited:
                        heapq.heappush(heap,(ne_cost+cost, nei))
            return -1






        

        


        